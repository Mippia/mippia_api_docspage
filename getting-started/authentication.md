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
curl https://platform.mippia.com/api/v1/ai-detection/standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -X POST \
  -F "file=@/path/to/your/track.mp3"
```

> ⚠️ **Warning:** Never share your API key publicly or commit it to version control.