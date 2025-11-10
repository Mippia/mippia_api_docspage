# Plagiarism Detection

Compare a track against a custom dataset to identify similar or potentially plagiarized music.

## Endpoint
```
POST /v1/plagiarism/check
```

## Parameters

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `dataset_id` | string | No | ID of the dataset to compare against, no dataset id refers to default dataset. |
| `target_audio_url` | string | Yes | URL of the track to analyze |

## Request Example
```bash
curl https://platform.mippia.com/v1/models/music-plagiarism-check \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "dataset_id": "dataset_abc123",
    "target_audio_url": "https://example.com/new-track.mp3"
  }'
```

## Response
```json
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "filename": "new-track.mp3",
  "filepath": "https://example.com/new-track.mp3",
  "model": "plagiarism",
  "created_at": "2025-11-09T10:30:00Z"
}
```

## Details

- **Supported audio length**: Up to 10 minutes
- **Processing time**: 3-4 minutes
- **Price**: $0.50 per request
- **Analysis includes**: Melody, rhythm, harmony, chord progressions

## How It Works

1. Upload your target track
2. Specify which dataset to compare against
3. Receive similarity scores and matching segments
4. Review matches with timestamps and reference tracks


:::{note}
Create custom datasets using the [Dataset Management API](dataset-management.md).
:::