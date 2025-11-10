# Webhooks

Configure webhooks to receive real-time notifications when processing completes.

## Setting Up Webhooks

1. Log in to your dashboard at [platform.mippia.com](https://platform.mippia.com)
2. Navigate to **Settings** > **Webhooks**
3. Click **Add Webhook**
4. Enter your webhook endpoint URL
5. Select which events to receive
6. Save and verify

## Webhook Events

### AI Detection Results

Triggered when AI detection analysis completes.

**Payload includes**:
- AI probability scores
- Confidence levels
- Analysis details

### Plagiarism Detection Results

Triggered when plagiarism detection completes.

**Payload includes**:
- Similarity scores
- Matching segments with timestamps
- Reference track information
- Detailed comparison metrics

### Lyric Plagiarism Results

Triggered when lyric analysis completes.

**Payload includes**:
- Similarity scores
- Matching lyric segments
- Semantic analysis details

## Webhook Security

All webhook requests include an `X-MIPPIA-Signature` header for verification.

### Verifying Signatures
```python
import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)
```

Your webhook secret is available in the dashboard under **Settings** > **Webhooks**.

## Best Practices

- Always verify webhook signatures
- Respond with `200 OK` quickly (within 5 seconds)
- Process webhook payloads asynchronously
- Implement retry logic for failed webhooks
- Monitor webhook delivery status in your dashboard

:::{tip}
Use webhooks instead of polling to reduce API calls and get results immediately.
:::