from redact.detector import Detector, Severity


def test_detects_aws_key_by_pattern():
    detector = Detector()
    line = 'aws_key_id = "AKIAFAKEKEYEXAMPLE12"\n'
    findings = detector.check_line("fake.py", 1, line)
    assert any(f.severity == Severity.HIGH and "AWS" in f.description for f in findings)


def test_detects_stripe_key_by_pattern():
    detector = Detector()
    stripe_prefix = "sk_live_"
    stripe_suffix = "abcd1234abcd1234abcd1234"
    line = f'stripe_key = "{stripe_prefix}{stripe_suffix}"\n'
    findings = detector.check_line("fake.py", 1, line)
    assert any("Stripe" in f.description for f in findings)


def test_detects_openai_key_by_pattern():
    detector = Detector()
    line = 'openai_key = "sk-fakekeyexample1234567890123456789012"\n'
    findings = detector.check_line("fake.py", 1, line)
    assert any("OpenAI" in f.description for f in findings)


def test_detects_high_entropy_secret_with_context():
    detector = Detector()
    line = 'db_password = "aB3!kZ9#mQ7$pL2@rT5&nW8*"\n'
    findings = detector.check_line("fake.py", 1, line)
    assert any(f.severity == Severity.MEDIUM for f in findings)


def test_clean_line_produces_no_findings():
    detector = Detector()
    line = 'print("Connecting to database...")\n'
    findings = detector.check_line("fake.py", 1, line)
    assert findings == []


def test_secret_is_masked_in_finding():
    detector = Detector()
    line = 'aws_key_id = "AKIAFAKEKEYEXAMPLE12"\n'
    findings = detector.check_line("fake.py", 1, line)
    finding = findings[0]
    assert finding.secret_masked.startswith("AK")
    assert "*" in finding.secret_masked
    assert "AKIAFAKEKEYEXAMPLE12" not in finding.secret_masked
