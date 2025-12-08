# Quick Start

Get started with MIPPIA API in minutes.

## Step 1: Get Your API Key

Sign up at [platform.mippia.com](https://platform.mippia.com) and generate your API key from the dashboard.


## Step 2: Setup Webhook

Set up a webhook endpoint to get results when processing completes. 


## Step 3: Make Your First Request

Detect if a track is AI-generated:
```bash
curl https://platform.mippia.com/api/v1/ai-detection/standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "file_path": "https://example.com/track.mp3",
  }'
```

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

## Step 4: Get the Response

When processing is complete, API will send a POST request to your configured webhook_url containing the detailed analysis result.
```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "status": "success",
  "model_type": "standard",
  "completed_at": "2025-12-04T05:30:15Z",
  "result": {
    "audio_filename.mp3": {
      "model_0": { 
        "overall_analysis": { 
          "prediction": "real", 
          "confidence": 0.923 
        } 
      },
      "model_1": {
        "segment_analysis": { 
          /* ... detailed array results ... */ 
        },
        "overall_analysis": { 
          "prediction": "real", 
          "confidence": 0.945 
        } 
      }
    }
  }
}
```

## Next Steps

- [Set up webhooks](../guides/webhooks.md)
- [View pricing](../resources/pricing.md)