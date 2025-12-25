# 🔒 Redact
> **A privacy-first pre-publish secret scanner for developers.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Privacy%20First-red)

## 🛑 The Problem
You're in the zone, building an amazing app. You temporarily paste an API key (AWS, OpenAI, Stripe) into your code for testing. You type `git commit` and `git push`, forgetting to remove it.

**Boom.** Your key is now public. Hackers find it in seconds. This can lead to massive bills or security breaches.

## ✅ The Solution: Redact
**Redact** is your local security guard. It lives in your project and scans your code *before* you commit. If it sees a secret, it **blocks the commit** and tells you exactly where the problem is.

- **🛡️ 100% Offline**: No data ever leaves your computer.
- **⚡ Super Fast**: Scans only changed lines during commits.
- **🧠 Hybrid Detection**: Smart enough to catch both known key formats and unknown random passwords.

---

## 🏎️ 1. Try it out (Quick Start)
*Do this if you just downloaded this repo and want to see Redact in action.*

### 1. Installation
```bash
git clone https://github.com/shivrajpatare/Redact.git
cd Redact
pip install -r requirements.txt
```

### 2. Run a Manual Scan
We've included a demo folder with fake secrets. Check it:
```bash
python run.py scan --path tests/demo
```
> **What happens?** Redact will find the fake keys in `tests/demo/unsafe_code.py` and print a report.

### 3. Test the "Auto-Block"
Activate the guard in this folder:
```bash
python run.py install-hook
```
Now try to commit the unsafe file:
```bash
git add tests/demo/unsafe_code.py
git commit -m "Testing Redact"
```
> **What happens?** Git will trigger Redact. Redact will see the keys and **STOP** the commit.

---

## 🛡️ 2. Protect YOUR Project
*Do this to add Redact protection to your own website, app, or bot.*

To protect another project (e.g., `my-cool-app`), follow these steps:

### Step 1: Clone Redact into your project
It's common to keep tools in a `tools/` folder:
```bash
cd my-cool-app
mkdir tools
git clone https://github.com/shivrajpatare/Redact.git tools/Redact
```

### Step 2: Install dependencies
```bash
pip install -r tools/Redact/requirements.txt
```

### Step 3: Activate the Guard
**Important:** Run this command from the **ROOT** of your project:
```bash
python tools/Redact/run.py install-hook
```

**You are now safe!** Every time you `git commit` in your app, Redact will automatically check your work.

---

## 🛠️ Features
- **Regex Detection**: AWS, Stripe, OpenAI, GitHub, Google, Slack, and Private Keys.
- **Entropy Analysis**: Catch random passwords even if they don't have a fixed format.
- **Context Awareness**: Flags strings assigned to variables like `API_KEY` or `PASSWORD`.
- **Masked Output**: Shows `AKIA****************` so your logs stay secret too.

## 📂 Project Structure
```text
Redact/
├── src/
│   ├── scanner.py    # File walker (respects .gitignore)
│   ├── detector.py   # Detection engine (Regex + Entropy)
│   ├── patterns.py   # Provider patterns
│   └── cli.py        # CLI Interface logic
├── run.py            # Main entry point
└── requirements.txt  # Project dependencies
```

## 🛡️ License
MIT License. Created by [Shivraj Patare](https://github.com/shivrajpatare). Stop the leaks!
