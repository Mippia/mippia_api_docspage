# Lyric Transcription

Extract lyrics from audio files using AI-powered speech recognition with multi-language support.

## Endpoint

```
POST /api/v1/lyric_transcription/{model}
```

## Parameters

### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model` | string | Yes | Transcription model name |

### Request Body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `file_path` | string | Yes | Path to the audio file in cloud storage |

## Request Example

### cURL

```bash
curl https://platform.mippia.com/api/v1/lyric_transcription/whisper \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "file_path": "uploads/audio/song.mp3"
  }'
```

### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/lyric_transcription/whisper"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "file_path": "uploads/audio/song.mp3"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## Response (Initial)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "status": "pending",
  "created_at": "2025-12-04T05:29:20Z"
}
```

## Callback Response (Success)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "task_name": "lyric_transcription",
  "status": "success",
  "completed_at": "2025-12-04T05:30:15Z",
  "result_json": {
    "lyrics": "I walk alone through empty streets\nSearching for a love I cannot find\nThe stars above remind me of your eyes\nBut you are gone and left me here behind",
    "languages": [
      {
        "code": "en",
        "probability": 0.9234
      },
      {
        "code": "ko",
        "probability": 0.0521
      },
      {
        "code": "ja",
        "probability": 0.0245
      }
    ],
    "is_instrumental": false
  }
}
```

## Callback Response (Instrumental Track)

When no vocals are detected, the track is classified as instrumental:

```json
{
  "task_id": "task_20251204052920_K9vPdq6a",
  "task_name": "lyric_transcription",
  "status": "success",
  "completed_at": "2025-12-04T05:30:15Z",
  "result_json": {
    "lyrics": "",
    "languages": [
      {
        "code": "Inst",
        "probability": 1.0
      }
    ],
    "is_instrumental": true
  }
}
```

## Callback Response (Failure)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "task_name": "lyric_transcription",
  "status": "failure",
  "completed_at": "2025-12-04T05:30:15Z",
  "result_json": {},
  "error": "Error message describing what went wrong"
}
```

## Result Fields

| Field | Type | Description |
| --- | --- | --- |
| `task_id` | string | Unique task identifier |
| `task_name` | string | Always `lyric_transcription` |
| `status` | string | Task status: `pending`, `processing`, `success`, `failure` |
| `completed_at` | string | ISO 8601 completion timestamp |
| `result_json` | object | Transcription results |
| `error` | string | Error message (only present when `status` is `failed`) |

### Result JSON Fields

| Field | Type | Description |
| --- | --- | --- |
| `lyrics` | string | Extracted lyrics text (empty if instrumental) |
| `languages` | array | Detected languages with probabilities (top 3) |
| `is_instrumental` | boolean | `true` if no vocals detected |

### Language Object Fields

| Field | Type | Description |
| --- | --- | --- |
| `code` | string | ISO 639-1 language code (or `Inst` for instrumental) |
| `probability` | float | Detection confidence (0.0 - 1.0) |

## Supported Languages

The transcription system supports 18 languages:

| Code | Language | Code | Language |
| --- | --- | --- | --- |
| `ko` | Korean | `ar` | Arabic |
| `en` | English | `hi` | Hindi |
| `zh` | Chinese | `th` | Thai |
| `ja` | Japanese | `vi` | Vietnamese |
| `es` | Spanish | `id` | Indonesian |
| `fr` | French | `tr` | Turkish |
| `de` | German | `pl` | Polish |
| `it` | Italian | `nl` | Dutch |
| `pt` | Portuguese | `ru` | Russian |

## Processing Pipeline

1. **Vocal Separation**: Audio is processed using Demucs to isolate vocals from instruments
2. **Vocal Detection**: Checks for presence of vocals using RMS and zero-crossing rate analysis
3. **Language Detection**: Multiple segments are analyzed to detect language distribution
4. **Transcription**: Whisper model transcribes the isolated vocals

## Notes

- **Supported formats**: mp3, wav, flac, m4a, aac, ogg
- **Processing time**: 1-3 minutes typical (depends on audio length)
- **Instrumental detection**: Tracks with no vocals or very short lyrics (<10 characters) are classified as instrumental
- **Multi-language support**: The system can detect mixed-language lyrics and reports the top 3 languages by probability
