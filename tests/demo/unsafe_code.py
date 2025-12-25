# This file contains fake secrets for testing the scanner

def connect_db():
    # TEST: High Entropy String with Context
    db_password = "xtu8#$2048(30948)slkdjf"
    return db_password

def send_request():
    # TEST: AWS Key Pattern (Modified to pass GitHub Push Protection)
    aws_key_id = "AKIA_FAKE_KEY_FOR_DEMO_12345"
    
    # TEST: Stripe Pattern
    stripe_key = "sk_live_FAKE_KEY_FOR_DEMO_12345"
    
    # TEST: OpenAI Pattern
    openai_key = "sk-FAKE-KEY-FOR-DEMO-12345678901234567890" 

    print("Connecting...")
