import re

PATTERNS = [
    {
        "name": "AWS Access Key",
        "regex": re.compile(r"(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}"),
        "severity": "HIGH",
        "confidence": "HIGH"
    },
    {
        "name": "GitHub Personal Access Token",
        "regex": re.compile(r"ghp_[0-9a-zA-Z]{36}"),
        "severity": "HIGH",
        "confidence": "HIGH"
    },
    {
        "name": "GitHub OAuth Access Token",
        "regex": re.compile(r"gho_[0-9a-zA-Z]{36}"),
        "severity": "HIGH",
        "confidence": "HIGH"
    },
    {
        "name": "Stripe Standard Live Key",
        "regex": re.compile(r"sk_live_[0-9a-zA-Z]{24}"),
        "severity": "HIGH",
        "confidence": "HIGH"
    },
    {
        "name": "OpenAI API Key (Approx)",
        "regex": re.compile(r"sk-[a-zA-Z0-9]{32,51}"), # Matches classic simplified pattern
        "severity": "HIGH",
        "confidence": "MEDIUM" # Higher false positive chance if not carefully bound
    },
    {
        "name": "Google API Key",
        "regex": re.compile(r"AIza[0-9A-Za-z\\-_]{35}"),
        "severity": "HIGH",
        "confidence": "HIGH"
    },
    {
        "name": "Slack Bot Token",
        "regex": re.compile(r"xoxb-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}"),
        "severity": "HIGH",
        "confidence": "HIGH"
    },
    {
        "name": "Private Key Block",
        "regex": re.compile(r"-----BEGIN (RSA|DSA|EC|PGP|OPENSSH) PRIVATE KEY-----"),
        "severity": "HIGH",
        "confidence": "HIGH"
    }
]
