# Webhooks

Configure webhooks to receive real-time notifications when processing completes.

## Setting Up Webhooks

1. Log in to your dashboard at [platform.mippia.com](https://platform.mippia.com)
2. Click **Callback URL**
3. [Prepare your webhook endpoint URL](#preparing-your-endpoint)
4. Enter your webhook endpoint URL
5. Save and verify

### Preparing Your Endpoint

Your endpoint must handle a challenge verification request. When you register a callback URL, MIPPIA sends the following POST request to your endpoint:

**Request from MIPPIA:**
```http
POST /your/webhook/endpoint HTTP/1.1
Content-Type: application/json

{
  "challenge": "generated-code-from-MIPPIA",
  "type": "url_verification"
}
```

**Your endpoint must respond:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "challenge": "generated-code-from-MIPPIA"
}
```

Once your endpoint returns the correct challenge value, registration is complete.

## Webhook Security

All webhook requests include two headers used for signature verification:

- `x-mippia-timestamp`: a timestamp indicating when the request was created (e.g. UNIX epoch seconds as a string).
- `x-mippia-signature`: an HMAC-SHA256 signature (hex string) computed over parts of the payload and the timestamp using a shared secret.

Verification overview:

1. Read `x-mippia-timestamp` and `x-mippia-signature` from the request headers.
2. Extract the payload field used for verification (for example, `task_id`).
3. Construct the signing string as `"{timestamp}:{task_id}"`.
4. Compute the expected signature using HMAC-SHA256 with the shared `secret_key`.
5. Compare the expected signature with the received signature using `hmac.compare_digest`.
6. To mitigate replay attacks, validate the timestamp is close to the current time (for example, within ±300 seconds).

### Example Verification Code
When MIPPIA sends a webhook to your endpoint, extract the headers and body, then verify the signature using a simple function that returns `True` if valid or `False` otherwise.

```python
import time
import hashlib
import hmac
from typing import Dict, Any

TIMESTAMP_TOLERANCE = 300  # seconds (5 minutes)


def is_valid_webhook(headers: Dict[str, str], body: Dict[str, Any], secret_key: str) -> bool:
    """Verify that an incoming webhook request is authentic.

    Args:
        headers: Request headers dict (e.g., from request.headers).
        body: Parsed JSON body dict (e.g., from request.json()).
        secret_key: Your shared secret key.

    Returns:
        True if the signature is valid and timestamp is within tolerance; False otherwise.
    """
    # 1) Extract required headers and payload field
    timestamp = headers.get("x-mippia-timestamp")
    signature = headers.get("x-mippia-signature")
    task_id = body.get("task_id")

    if not (timestamp and signature and task_id):
        return False

    # 2) Validate timestamp (prevent replay attacks)
    try:
        ts = int(timestamp)
    except (ValueError, TypeError):
        return False

    now = int(time.time())
    if abs(now - ts) > TIMESTAMP_TOLERANCE:
        return False

    # 3) Compute expected signature: "{timestamp}:{task_id}"
    sign_data = f"{timestamp}:{task_id}"
    expected_signature = hmac.new(
        key=secret_key.encode("utf-8"),
        msg=sign_data.encode("utf-8"),
        digestmod=hashlib.sha256
    ).hexdigest()

    # 4) Constant-time comparison
    return hmac.compare_digest(expected_signature, signature)
```

Key points:

- The function takes three arguments: `headers` (dict), `body` (dict), and `secret_key` (str).
- It extracts `x-mippia-timestamp` and `x-mippia-signature` from the headers.
- It validates the timestamp to prevent replay attacks (within ±300 seconds).
- It computes the expected signature from `"{timestamp}:{task_id}"` using HMAC-SHA256.
- It safely compares the expected signature with the received signature using `hmac.compare_digest`.
- Returns `True` if valid, `False` otherwise.

Notes and best practices:

- The field used for signature generation (`task_id` in these examples) must match the convention MIPPIA uses when sending webhooks.
- Protect your secret key. Store it in environment variables or a secrets manager—do not hard-code it in source control.
- Always use HTTPS for your webhook endpoints to protect the transport layer.
- Use constant-time comparison (`hmac.compare_digest`) to avoid timing attacks when comparing signatures.
