# 🔒 Redact
> **A privacy-first pre-publish secret scanner for developers.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Privacy%20First-red)

## 🛑 The Problem
You are building an amazing app. You accidentally paste an AWS key or OpenAI API key into your code. You type `git commit` and `git push`.
**Boom.** Your key is now public. Hackers find it in seconds. You wake up to a $5,000 bill.

## ✅ The Solution: Redact
**Redact** is a simple guard dog that lives in your project. It checks your code *before* you commit.
If it sees a secret, it **blocks the commit** and tells you exactly where the problem is.

- **Offline**: No data ever leaves your computer.
- **Fast**: Scans only what you touch.
- **Privacy-First**: It stops the leak securely on your machine.

---

## 📖 How to Use (Integration Guide)

Do you want to protect your own project (e.g., a website, app, or bot)? Follow these 3 steps:

### 1. Download Redact
Go to your project's root folder and download Redact into a `tools` folder:
```bash
# Inside your project folder
mkdir tools
git clone https://github.com/shivrajpatare/Redact.git tools/Redact
```

### 2. Install
Install the required python libraries:
```bash
pip install -r tools/Redact/requirements.txt
```

### 3. Activate Protection 🛡️
Run the installer. This will tell Git to ask Redact for permission before every commit.
```bash
python tools/Redact/run.py install-hook
```

**That's it! You are safe.**
Try trying to commit a fake key like `AKIAFAKEKEYEXAMPLE12` and watch Redact stop you!

---

## 🛠️ Advanced Usage

### Manual Scanning
If you just want to scan a folder once to check for leaks:
```bash
python tools/Redact/run.py scan --path src/
```

### Features
- **Regex Detection**: AWS, Stripe, OpenAI, GitHub, Google, Slack keys.
- **Entropy Analysis**: Finds unknown high-entropy strings (passwords, tokens).
- **Secure Output**: automatically masks secrets `sk-proj-****` in the terminal.

## 📂 Project Structure
```text
Redact/
├── src/
│   ├── scanner.py    # Recursive file walker
│   ├── detector.py   # Detection engine (Regex + Entropy)
│   ├── patterns.py   # Secret regex definitions
│   └── cli.py        # Command-line interface
├── run.py            # Entry point
└── requirements.txt  # Dependencies
```

## 🛡️ License
MIT License. Free to use in any private or public project.
