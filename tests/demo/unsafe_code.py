# This file contains fake secrets for testing the scanner

def connect_db():
    # TEST: High Entropy String with Context
    db_password = "xtu8#$2048(30948)slkdjf"
    return db_password

def send_request():
    # TEST: AWS Key Pattern
    aws_key_id = "AKIAIMADEUPKEY123456"
    
    # TEST: Stripe Pattern
    stripe_key = "sk_live_m4d3upk3y123456789012345"
    
    # TEST: OpenAI Pattern
    openai_key = "sk-7n9871239871239871239871239871239871239871239871" 

    print("Connecting...")
