from dataclasses import dataclass
from enum import Enum
import re
from .patterns import PATTERNS

class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

@dataclass
class Finding:
    file_path: str
    line_number: int
    secret_masked: str
    description: str
    severity: Severity

from .utils import calculate_shannon_entropy

class Detector:
    def __init__(self):
        self.patterns = PATTERNS
        self.context_keywords = re.compile(r'(api[_-]?key|secret|password|token|auth|credential)', re.IGNORECASE)
        # Capture content inside quotes
        self.string_literal_regex = re.compile(r'("|\')(?P<content>.*?)(\1)')

    def check_line(self, file_path: str, line_num: int, content: str) -> list[Finding]:
        findings = []
        
        # 1. Regex Pattern Check
        for pattern in self.patterns:
            matches = pattern['regex'].finditer(content)
            for match in matches:
                secret = match.group()
                findings.append(self._create_finding(file_path, line_num, secret, 
                    f"Potential {pattern['name']} detected", Severity[pattern['severity']]))

        # 2. Entropy + Context Check
        # Only run if finding list is empty to avoid double reporting or noise? 
        # Actually better to run it but dedupe later. For MVP, let's run it.
        findings.extend(self._check_entropy(file_path, line_num, content))
        
        return findings

    def _check_entropy(self, file_path: str, line_num: int, content: str) -> list[Finding]:
        results = []
        # Optimization: Early exit if no assignment or context keyword in line
        # This reduces false positives significantly.
        if not self.context_keywords.search(content):
            return []

        for match in self.string_literal_regex.finditer(content):
            candidate = match.group('content')
            if len(candidate) < 10: # Ignore short strings
                continue
            
            # Allowlist check (basic)
            if ' ' in candidate: # Secrets usually don't have spaces (except passphrases, but ignoring for now to reduce noise)
                continue

            entropy = calculate_shannon_entropy(candidate)
            # Threshold: 4.5 is a common heuristic for base64/random strings
            if entropy > 4.5:
                results.append(self._create_finding(file_path, line_num, candidate,
                    f"High entropy string detected ({entropy:.2f}) with suspicious context", Severity.MEDIUM))
        return results

    def _create_finding(self, file_path, line_num, secret, description, severity):
        if len(secret) > 4:
            masked = secret[:2] + '*' * (len(secret) - 4) + secret[-2:]
        else:
            masked = '*' * len(secret)
        
        return Finding(
            file_path=file_path,
            line_number=line_num,
            secret_masked=masked,
            description=description,
            severity=severity
        )
