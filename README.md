# Secret Scanner Benchmark Test Repository

⚠️ **WARNING**: This repository contains intentional secrets for testing purposes.
These are NOT real credentials and should not be used for any actual services.

## Purpose

This repository is designed to benchmark secret scanning tools by providing:
- **150 unique secrets** with properly verified formats across 11 categories
- **28 false positive patterns** (sequential, repeating, low entropy)
- **Multiple file formats** (Python, JavaScript, TypeScript, YAML, JSON, .env, PEM)
- **Realistic code contexts** with secrets embedded naturally

## Verified Secret Formats

All secrets have been generated with **verified formats** based on official documentation:

- **Stripe**: `sk_live_51...` (107 chars total)
- **GitHub PAT**: `ghp_...` (40 chars total)
- **OpenAI**: `sk-...` (51 chars total)
- **AWS Access Key**: `AKIA...` (20 chars total)
- And 146 more with correct lengths and patterns

## Categories (150 Secrets)

1. **Payment** (8): Stripe, PayPal, Square, Braintree, Adyen
2. **AI/ML** (10): OpenAI, Anthropic, HuggingFace, Cohere, Replicate, etc.
3. **Cryptographic Keys** (12): RSA, EC, AES, HMAC, encryption keys
4. **Cloud** (20): AWS, GCP, Azure, DigitalOcean, Heroku, etc.
5. **Database** (15): PostgreSQL, MySQL, MongoDB, Redis, etc.
6. **Communication** (15): Slack, Discord, Telegram, Twilio, SendGrid, etc.
7. **CI/CD** (20): GitHub, GitLab, NPM, PyPI, CircleCI, etc.
8. **SaaS** (20): Datadog, Sentry, Auth0, Okta, Figma, etc.
9. **Authentication** (15): JWT, OAuth, Session, Cookie, LDAP, etc.
10. **Blockchain** (10): Infura, Alchemy, Etherscan, Coinbase, etc.
11. **Miscellaneous** (5): Mapbox, Google Maps, Weather API, etc.

## False Positives (28)

Intentional false positive patterns that should NOT be detected:
- Sequential: `12345678`, `AKIA0123456789ABCDEF`
- Repeating: `00000000`, `aaaaaaa`
- Low Entropy: `password123`, `testkey000`
- Common Hex: `deadbeef`, `cafebabe`
- Base64 Simple: `dGVzdA==` (base64 of "test")

## Structure

```
test-repo/
├── src/
│   ├── python/          # 9 Python files with secrets
│   ├── javascript/      # 1 JS file
│   └── typescript/      # 1 TS file
├── config/
│   ├── env/            # .env file
│   ├── yaml/           # YAML config
│   ├── json/           # JSON config
│   └── pem/            # PEM private keys
└── edge-cases/
    └── false_positives.py  # False positive patterns
```

## Usage

### Test Your Scanner

```bash
# Scan the repository
your-scanner scan test-repo/

# Expected results:
# - Should detect: 150 real secrets
# - Should ignore: 28 false positives
# - Detection rate: aim for >90%
```

### Compare with TruffleHog

```bash
trufflehog git file://./test-repo --json --no-verification
```

## Statistics

- **Total Secrets**: 150 (all with verified formats)
- **File Types**: Python, JavaScript, TypeScript, YAML, JSON, .env, PEM
- **Secret Types**: 150+ unique formats
- **False Positives**: 28 realistic patterns
- **Files**: 17 files with embedded secrets

## Key Improvements Over Previous Version

1. ✅ **Correct Stripe Keys**: 107 chars (`sk_live_51...` + 99 random chars)
2. ✅ **Verified OpenAI**: 51 chars (`sk-` + 48 chars)
3. ✅ **Proper Anthropic**: 109 chars (`sk-ant-api03-` + 96 chars)
4. ✅ **Realistic AWS**: 20-char access keys, 40-char secret keys
5. ✅ **All formats validated** against official documentation

## License

MIT - This is a testing tool for security research.

---

Generated with verified secret formats for accurate benchmarking.
