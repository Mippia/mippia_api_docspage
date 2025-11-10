# Authentication

All API requests require authentication using an API key.

## Getting Your API Key

1. Sign up at [platform.mippia.com](https://platform.mippia.com)
2. Navigate to your dashboard
3. Go to Settings > API Keys
4. Generate a new API key
5. Copy and store it securely

## Using Your API Key

Include your API key in the `Authorization` header for all requests:
```http
Authorization: Bearer YOUR_API_KEY
```

## Example Request
```bash
curl https://api.mippia.com/v1/models/ai-detection-standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "file_path": "https://example.com/track.mp3",
    "filename": "track.mp3"
  }'
```

:::{warning}
Never share your API key publicly or commit it to version control.
:::