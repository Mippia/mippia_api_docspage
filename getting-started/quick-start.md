# Quick Start

Get started with MIPPIA API in minutes.

## Step 1: Get Your API Key

Sign up at [platform.mippia.com](https://platform.mippia.com) and generate your API key from the dashboard.

## Step 2: Make Your First Request

Detect if a track is AI-generated:
```bash
curl https://platform.mippia.com/v1/models/ai-detection-standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "file_path": "https://example.com/track.mp3",
    "filename": "track.mp3"
  }'
```

## Step 3: Get the Response

You'll receive a task ID:
```json
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "filename": "track.mp3",
  "model": "standard",
  "created_at": "2025-11-09T10:30:00Z"
}
```

## Step 4: Receive Results

Set up a webhook or poll the status endpoint to get results when processing completes.

## Next Steps

- [Learn about AI Detection models](../api-reference/ai-detection.md)
- [Set up webhooks](../guides/webhooks.md)
- [View pricing](../resources/pricing.md)