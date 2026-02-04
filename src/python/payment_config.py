# Payment Processing Configuration
import stripe
import paypal

# Stripe Configuration
STRIPE_LIVE_KEY = "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"
STRIPE_TEST_KEY = "sk_test_51h57FmwKeEjOUQzEoDxsPoeSpfzkipCSdPVzn185Mh9iiKUaBYK7ZFyLpmU6NlXddahBumFIRvcLgRjf6ylnD7znPZ0xTEGR12"
STRIPE_RESTRICTED_KEY = "rk_live_NIyKPSUd2j4tBbzFDqIUqfLK"
STRIPE_WEBHOOK_SECRET = "whsec_pICgAqDxvXbrpXG5DopW7OOJWHC1hWrq"

# PayPal Configuration
PAYPAL_CLIENT_ID = "ncjhzBvyJIzYbTARk0RHQxQx4VbEDhB2Q0ftfSsP9MEgbWVrOajwNhfGzLlsmkNpagJeW4LsUyQ2KDXM"

# Square Configuration
SQUARE_ACCESS_TOKEN = "sq0atp-E27VK2SZaRRRTqhI07Fgrq"

# Braintree Configuration
BRAINTREE_PRIVATE_KEY = "Kgu2Ctc9THb06XCPHTIT9eMB3fTZ5hw9"

# Adyen Configuration
ADYEN_API_KEY = "RFVzeqmLpq6hEDmziJMjGwtE5soAU4brt2go420K"

# OpenAI Configuration
OPENAI_API_KEY = "sk-Qk8C5dEF6DVT1GTvGwW0WG5JzcFbUS1o2CMXwssjgAtV7FyR"
OPENAI_ORG_KEY = "org-YgaTOiakW8H0QSQFQFNItDlN"

# Anthropic Configuration
ANTHROPIC_API_KEY = "sk-ant-api03-R0lSLvFUAnHBnS3KM7Cw0VIBfFXoqRgd4bHCGGH36DvjRhMy5DAszqHOUkHq9Mdnfl7lvHCM6NsWFAmSVnHk7at49SXkcz5n"

# HuggingFace
HUGGINGFACE_TOKEN = "hf_3OsJNHHTTl9Q9R2Chlyz9k9aYH7P9WV37E"

# Other AI services
COHERE_API_KEY = "KhR66irgtJYk6l5C3NTDwJxkG5jQU1cy5IaFEoPY"
REPLICATE_TOKEN = "r8_EoPKcMvH390GvPNHvRpzfms50Tly9H3NehbGFuvE"
STABILITY_AI_KEY = "sk-EGUSOdyIKCfMPytOApqc17bEV2A6AjI41aJcSk46uGnB9rVGPcXhLbvylL2Fmrl9"
ELEVENLABS_API_KEY = "42be18b453b2cdd89a2df8bb16afe4b3f7636c92a8fa382db20825da92879672"
TOGETHER_AI_KEY = "fb3e6dcd495832e73c7dd57a7bc577c6ccf9174c9c2538cf42cad861fb143336"
ANYSCALE_TOKEN = "esecret_7IRTkBcgjaVDTnSilJIqsBxJVrvsZeu5IGK6pvo7"

def process_payment(amount, card):
    stripe.api_key = STRIPE_LIVE_KEY
    return stripe.Charge.create(amount=amount, source=card)
