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

All webhook requests include an `X-MIPPIA-Signature` header for verification.
