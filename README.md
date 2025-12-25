# 🔒 Redact
> **A privacy-first pre-publish secret scanner for developers.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Privacy%20First-red)

## 🛑 The Problem
You're deep in your zone, building an amazing app. You temporarily paste an AWS key or OpenAI API key into your code for testing. You type `git commit` and `git push`, forgetting to remove it.

**Boom.** Your key is now public. Hackers find it in seconds. You wake up to a $5,000 bill.

## ✅ The Solution: Redact
**Redact** is your local guard dog. It lives in your project and sniffs your code *before* you commit. If it sees a secret, it **blocks the commit** and highlights the exact line.

- **🛡️ 100% Offline**: No data ever leaves your computer.
- **⚡ Lightning Fast**: Scans only changed files during git commits.
- **🧠 Hybrid Detection**: Uses Regex for known keys and Entropy Analysis for unknown passwords.

---

## 🚀 Quick Start (Walkthrough)

Let's see Redact in action. follow these 3 steps to verify it works right now.

### 1. Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/shivrajpatare/Redact.git
cd Redact
pip install -r requirements.txt
```

### 2. Manual Scan (The Demo)
We have a `tests/demo` folder with fake secrets. Let's scan it:
```bash
python run.py scan --path tests/demo
```
**Expected Result:**
You should see Redact flag the fake AWS, Stripe, and OpenAI keys with a **[HIGH]** severity warning.

### 3. Git Protection (The Hook)
Install the pre-commit hook into this repo:
```bash
python run.py install-hook
```
Now, try to commit the unsafe demo file:
```bash
git add tests/demo/unsafe_code.py
git commit -m "Testing Redact"
```
**Expected Result:**
Your terminal will show `❌ Secrets detected! Commit blocked.`. Redact just saved you from a leak!

---

## 📖 How to Protect YOUR Project

Do you want to shield your own app/website? It takes 60 seconds.

### Step-by-Step Integration:
1.  **Navigate** to your project's root folder.
2.  **Download** Redact into a subfolder:
    ```bash
    mkdir tools
    git clone https://github.com/shivrajpatare/Redact.git tools/Redact
    ```
3.  **Install** dependencies: `pip install -r tools/Redact/requirements.txt`
4.  **Activate**: Run the installer:
    ```bash
    python tools/Redact/run.py install-hook
    ```

**You are now protected.** Any future `git commit` in your project will be automatically scanned by Redact.

---

## 🛠️ Features
- **Regex Detection**: AWS, Stripe, OpenAI, GitHub, Google, Slack, and Private Keys.
- **Entropy Analysis**: Smart heuristics to find high-randomness strings (passwords/tokens).
- **Context Awareness**: Flags strings assigned to variables like `API_KEY` or `SECRET`.
- **Masked Output**: Displays `AKIA****************` to keep your logs clean.

## 📂 Project Structure
```text
Redact/
├── src/
│   ├── scanner.py    # Recursive file walker (respects .gitignore)
│   ├── detector.py   # Hybrid engine (Regex + Entropy)
│   ├── patterns.py   # Database of secret patterns
│   └── cli.py        # Interactive CLI
├── run.py            # Entry point
└── requirements.txt  # Dependencies
```

## 🛡️ License
MIT License. Created by [Shivraj Patare](https://github.com/shivrajpatare). Feel free to use in any project!
