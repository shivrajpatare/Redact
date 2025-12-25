# This file contains fake secrets for testing the scanner

def connect_db():
    # TEST: High Entropy String with Context
    db_password = "xtu8#$2048(30948)slkdjf"
    return db_password

def send_request():
    # TEST: AWS Key Pattern (Fake but matches Regex: AKIA + 16 alphanumeric)
    aws_key_id = "AKIAFAKEKEYEXAMPLE12"
    
    # TEST: Stripe Pattern (Fake but matches Regex: sk_live_ + 24 alphanumeric)
    stripe_key = "sk_live_fakekeyexample12345678"
    
    # TEST: OpenAI Pattern (Fake but matches Regex: sk- + 32 alphanumeric)
    openai_key = "sk-fakekeyexample1234567890123456789012" 

    print("Connecting...")
