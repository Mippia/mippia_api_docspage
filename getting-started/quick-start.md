# Quick Start

Get started with MIPPIA API in minutes.

## Step 1: Get Your API Key

Sign up at [platform.mippia.com](https://platform.mippia.com) and generate your API key from the dashboard.


## Step 2:  Upload Your Track
Get a `musicId` by uploading your audio file

```bash
curl https://platform.mippia.com/api/v1/music \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@/path/to/your/track.mp3"
```
You'll receive a music ID:
```json
{
  "musicId": "cd75b87f-cad9-4dfd-a49f-8a2d34408a0e",
  "title": "track",
  "created_at": "2025-12-10T02:18:01Z"
}
```

## Step 3: Make Your First Request

Detect if a track is AI-generated:

```bash
curl https://platform.mippia.com/api/v1/ai-detection/standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"musicId": "cd75b87f-cad9-4dfd-a49f-8a2d34408a0e"}'
```

You'll receive a task ID:

```json
{
  "taskId": "task_20251210021802_AjHwAeUR"
}
```

## Step 4: Get Results

You can receive results in two ways:

### Option A: Webhook (Recommended)

Set up a webhook endpoint in your dashboard. When processing completes, we'll send a POST request to your configured URL:

```json
{
  "taskResultId": 34,
  "title": "track",
  "aiModelName": "standard",
  "url": "/api/v1/ai-detection/standard",
  "taskId": "task_20251210021802_AjHwpPUR",
  "requestedAt": "2025-12-10T02:18:01.327867Z",
  "completedAt": null,
  "status": "processing",
  "result": {
    "track.mp3": {
      "model_0": { 
        "overall_analysis": { 
          "prediction": "real", 
          "confidence": 0.923 
        } 
      },
      "model_1": {
        "segment_analysis": { /* ... */ },
        "overall_analysis": { 
          "prediction": "real", 
          "confidence": 0.945 
        } 
      }
    }
  }
}
```

### Option B: Polling

Poll the task result endpoint until processing completes:

```bash
curl https://platform.mippia.com/api/v1/task/result/task_20251210021802_AjHwAeUR \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The polling response has the same envelope as the webhook payload: task metadata at the
top level and the worker output under `result`. Until the task starts, `result` is `null`.

**Pending response:**

```json
{
  "taskResultId": 34,
  "title": "track",
  "aiModelName": "standard",
  "url": "/api/v1/ai-detection/standard",
  "taskId": "task_20251210021802_AjHwAeUR",
  "requestedAt": "2025-12-10T02:18:01.327867Z",
  "completedAt": null,
  "status": "pending",
  "result": null,
  "ppc": { "final": 0.0 }
}
```

**Completed response:** the worker output sits under `result`, so the scores are at
`result.result` (for AI detection keyed by filename; for plagiarism see the
`signature`/`vocal`/`inst`/`topline`/`total_scores` keys).

```json
{
  "taskResultId": 34,
  "title": "track",
  "aiModelName": "standard",
  "url": "/api/v1/ai-detection/standard",
  "taskId": "task_20251210021802_AjHwAeUR",
  "requestedAt": "2025-12-10T02:18:01.327867Z",
  "completedAt": "2025-12-10T02:18:16.102331Z",
  "status": "success",
  "ppc": { "final": 0.0 },
  "result": {
    "task_id": "task_20251210021802_AjHwAeUR",
    "status": "success",
    "status_code": 200,
    "error": null,
    "model_type": "standard",
    "completed_at": "2025-12-10T02:18:15Z",
    "result": {
      "track.mp3": {
      "model_0": { 
        "overall_analysis": { 
          "prediction": "real", 
          "confidence": 0.923 
        } 
      },
      "model_1": {
        "segment_analysis": { /* ... */ },
        "overall_analysis": { 
          "prediction": "real", 
          "confidence": 0.945 
        } 
      }
    }
    }
  }
}
```

> **Tip:** We recommend polling every 5-10 seconds. AI detection typically completes in
> 15-60 seconds; plagiarism detection runs a full library comparison and typically takes
> 5-10 minutes. Wait for the top-level `status` to become `success`.


## Next Steps

- [Set up webhooks](../guides/webhooks.md)
- [API Reference](../api-reference/ai-detection.md)