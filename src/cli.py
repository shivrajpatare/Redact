import click
import sys
import os
import stat
import colorama
from colorama import Fore, Style
from .scanner import Scanner
from .detector import Detector, Severity

colorama.init()

@click.group()
def cli():
    """secret-scanner: A privacy-first tool to detect exposed secrets."""
    pass

@cli.command()
@click.option('--path', default='.', help='Path to scan directory')
@click.option('--verbose', is_flag=True, help='Show detailed progress')
def scan(path, verbose):
    """Recursively scan a directory for secrets."""
    click.echo(f"{Style.BRIGHT}Starting Secret Scanner...{Style.RESET_ALL}\n")
    
    scanner = Scanner(path)
    detector = Detector()
    
    issues_found = 0
    
    for file_path in scanner.scan():
        if verbose:
            click.echo(f"Scanning: {file_path}", nl=True)
            
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, line in enumerate(f, 1):
                    findings = detector.check_line(file_path, i, line)
                    if findings:
                        for finding in findings:
                            issues_found += 1
                            print_finding(finding)
        except Exception as e:
            if verbose:
                click.echo(f"{Fore.RED}Error reading {file_path}: {e}{Style.RESET_ALL}")

    print_summary(issues_found)
    
    if issues_found > 0:
        sys.exit(1)

@cli.command('install-hook')
def install_hook():
    """Install the pre-commit hook."""
    hook_path = os.path.join('.git', 'hooks', 'pre-commit')
    
    if not os.path.exists('.git'):
        click.echo(f"{Fore.RED}Error: Not a git repository. Run 'git init' first.{Style.RESET_ALL}")
        sys.exit(1)
        
    # Python script that the hook will execute
    # We use the absolute path to the current python executable to ensure environment consistency
    hook_script = f"""#!/bin/sh
echo "🔒 Secret Scanner checking your changes..."
# Run the scanner on the current directory
"{sys.executable}" "{os.path.abspath(sys.argv[0])}" scan --path .

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    echo "❌ Secrets detected! Commit blocked."
    exit 1
fi
echo "✅ No secrets found."
exit 0
"""
    
    try:
        # Force LF line endings for shell script compatibility on Windows (Git Bash)
        with open(hook_path, 'w', newline='\n', encoding='utf-8') as f:
            f.write(hook_script)
        
        # Make executable (unix) - on Windows this might fail or be unnecessary, so we wrap it
        try:
            st = os.stat(hook_path)
            os.chmod(hook_path, st.st_mode | stat.S_IEXEC)
        except Exception:
            pass # Ignore chmod errors on Windows
        
        click.echo(f"{Fore.GREEN}Success: Pre-commit hook installed at {hook_path}{Style.RESET_ALL}")
    except Exception as e:
         click.echo(f"{Fore.RED}Error: Failed to install hook: {e}{Style.RESET_ALL}")
         sys.exit(1)

def print_finding(finding):
    color = Fore.RED if finding.severity == Severity.HIGH else Fore.YELLOW
    
    click.echo(f"{color}[{finding.severity.name}] {finding.description}{Style.RESET_ALL}")
    click.echo(f"  File: {finding.file_path}:{finding.line_number}")
    click.echo(f"  Secret: {finding.secret_masked}")
    click.echo("")

def print_summary(count):
    click.echo("-" * 40)
    if count == 0:
        click.echo(f"{Fore.GREEN}No secrets found. Good job!{Style.RESET_ALL}")
    else:
        click.echo(f"{Fore.RED}Scan Complete: {count} potential issues found.{Style.RESET_ALL}")

