# False Positives - These should NOT be detected as real secrets

# Sequential patterns
SEQUENTIAL_DIGITS = "12345678901234567890"
SEQUENTIAL_HEX = "0123456789ABCDEF0123456789ABCDEF"
SEQUENTIAL_ALPHA = "abcdefghijklmnopqrstuvwxyz"
FAKE_AWS_KEY = "AKIA0123456789ABCDEF"
FAKE_GITHUB_PAT = "ghp_0123456789abcdefghijklmnopqrstuvwxyz"
FAKE_STRIPE_KEY = "sk_live_0123456789abcdef"

# Repeating patterns
ALL_ZEROS = "00000000000000000000"
ALL_ONES = "11111111111111111111"
ALL_A = "aaaaaaaaaaaaaaaaaaaa"
ALL_F = "ffffffffffffffffffffffff"
REPEATED_ABC = "abcabcabcabcabcabcab"
FAKE_SLACK_TOKEN = "xoxb-000000000000-000000000000-000000000000000000000000"

# Low entropy
PASSWORD = "password123"
TEST_KEY = "testkey000"
ADMIN_PASSWORD = "admin123"
SECRET = "secret123"
API_KEY_TEST = "apikey_test_123456"
DEFAULT_KEY = "default_encryption_key"
SAMPLE_TOKEN = "sample_token_value"

# Common hex patterns
DEADBEEF = "deadbeefdeadbeefdeadbeefdeadbeef"
CAFEBABE = "cafebabecafebabecafebabecafebabe"
FEEDFACE = "feedfacefeedfacefeedfacefeedface"
BAADF00D = "baadf00dbaadf00dbaadf00dbaadf00d"
C0FFEE = "c0ffee00c0ffee00c0ffee00c0ffee00"

# Base64 of simple strings
TEST_B64 = "dGVzdA=="  # base64 of "test"
ADMIN_B64 = "YWRtaW4="  # base64 of "admin"
PASSWORD_B64 = "cGFzc3dvcmQ="  # base64 of "password"
SECRET_B64 = "c2VjcmV0"  # base64 of "secret"
