# 🔒 Secret Scanner CLI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Privacy%20First-red)

A privacy-first, offline DevSecOps tool to prevent secret leaks in your code.
Designed for developers who want to stop accidental API key exposures before they happen.

## 🚀 Why this tool?
Developers often accidentally commit keys (AWS, OpenAI, Stripe) to public repositories. This tool scans your code *locally* before it leaves your machine.
- **🛡️ Offline**: No data ever leaves your laptop.
- **⚡ Fast**: Scans recursively, respecting `.gitignore`.
- **🧠 Smart**: Detects known patterns (Regex) and suspicious high-entropy strings (Heuristics).

## ✨ Features
- **Regex Detection**: AWS, Stripe, OpenAI, GitHub, Google, Slack keys.
- **Entropy Analysis**: Finds unknown high-entropy strings (passwords, tokens).
- **Git Integration**: Built-in `pre-commit` hook to block unsafe commits.
- **Secure Output**: Automatically masks secrets in standard output.

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/secret-scanner.git
cd secret-scanner
pip install -r requirements.txt
```

## 💻 Usage

### 1. Manual Scan
Scan your current project directory:
```bash
python run.py scan
```

Scan a specific folder:
```bash
python run.py scan --path /path/to/project
```

### 2. Git Pre-commit Hook (Recommended)
Protect your repo from accidental leaks so you never commit a secret again:
```bash
# Installs a hook into .git/hooks/pre-commit
python run.py install-hook
```
Now `git commit` will automatically scan your changes and block the commit if secrets are found.

## 📂 Project Structure

```text
secret-scanner/
├── src/
│   ├── scanner.py    # File traversal logic (respects .gitignore)
│   ├── detector.py   # Hybrid detection engine (Regex + Entropy)
│   ├── patterns.py   # Regex definitions for major providers
│   ├── utils.py      # Math helpers (Shannon Entropy)
│   └── cli.py        # Command-line interface
├── tests/            # Demo suite
├── run.py            # Entry point
└── requirements.txt  # Dependencies
```

## 🛡️ License
MIT License. Free to use and modify.
