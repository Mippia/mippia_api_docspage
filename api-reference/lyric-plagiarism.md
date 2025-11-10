# Lyric Plagiarism Detection

Analyze semantic similarity between lyrics using multilingual text understanding.

## Endpoint
```
POST /v1/lyric_plagiarism/{model}
```

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | string | Yes | Model name for lyric analysis |

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `lyric_text` | string | Yes | Lyrics to analyze |
| `song_title` | string | No | Title of the song (optional) |

## Request Example
```bash
curl https://platform.mippia.com/v1/models/lyric-plagiarism-semantic \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "lyric_text": "Your lyrics here...",
    "song_title": "Song Title"
  }'
```

## Response
```json
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "filename": "Song Title",
  "model": "semantic",
  "created_at": "2025-11-09T10:30:00Z"
}
```

## Details

- **Status**: Currently in Beta (free during beta period)
- **Language support**: 100+ languages
- **Processing time**: 10-30 seconds
- **Analysis method**: Semantic similarity using advanced NLP

:::{important}
This API is currently in Beta and is free to use. Pricing will be announced before general availability.
:::