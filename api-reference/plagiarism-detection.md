# Music Plagiarism Detection

Detect potential music plagiarism by comparing audio against a database of existing songs using structural music analysis.

## Endpoint

```
POST /api/v1/plagiarism/{model_name}
```

## Parameters

### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model_name` | string | Yes | Model to use: `standard` |

### Request Body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | binary | Yes | Audio file to analyze (mp3, wav, flac, m4a, aac, ogg) |
| `dataset_id` | string | No | Dataset ID for comparison, 'default' is only option available for now. |

## Request Example

### cURL

```bash
curl https://platform.mippia.com/api/v1/plagiarism/standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -X POST \
  -F "file=@/path/to/audio.mp3" \
  -F "dataset_id=default"
```

### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/plagiarism/standard"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
files = {
    "file": open("/path/to/audio.mp3", "rb")
}
data = {
    "dataset_id": "default"
}

response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
```

## Response (Initial)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "status": "pending",
  "filepath": "uploads/task_20251204052920_J8uNdq5z.mp3",
  "model": "standard",
  "created_at": "2025-12-04T05:29:20Z"
}
```

## Callback Response (Processing)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "task_type": "plagiarism_detection",
  "status": "processing",
  "result": null,
  "started_at": "2025-12-04T05:29:25Z"
}
```

## Callback Response (Completed)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "task_type": "plagiarism_detection",
  "status": "success",
  "completed_at": "2025-12-04T05:30:45Z",
  "result": {
    "signature": [
      {
        "signature_metric": 0.7525,
        "original": {
          "title": "My New Song",
          "link": null,
          "time_start": 7.42,
          "time_end": 14.81,
          "key": "G major",
          "chords": ["N", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj", "D:maj"]
        },
        "comparison": {
          "title": "Similar Existing Song",
          "link": "https://www.youtube.com/watch?v=example",
          "time_start": 94.38,
          "time_end": 102.12,
          "key": "E minor",
          "chords": ["E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min", "E:min"]
        },
        "scores": {
          "vocal": {
            "metric": 1,
            "pitch_score": 0.665,
            "correlation": 0.889,
            "ratio": 0.796,
            "bpm_ratio": 0.967,
            "difficulty": 0.731
          },
          "melody": {
            "metric": 0,
            "pitch_score": 0,
            "correlation": 0,
            "ratio": 0,
            "bpm_ratio": 0.967,
            "difficulty": 0.047
          },
          "topline": {
            "metric": 0.875,
            "pitch_score": 0.444,
            "correlation": 0.923,
            "ratio": 0.780,
            "bpm_ratio": 0.967,
            "difficulty": 0.5
          },
          "chord": 0
        }
      }
    ],
    "vocal": [...],
    "inst": [...],
    "topline": [...]
  }
}
```

## Result Fields

| Field | Type | Description |
| --- | --- | --- |
| `task_id` | string | Unique task identifier |
| `task_type` | string | Task type: `plagiarism_detection` |
| `status` | string | Task status: `pending`, `processing`, `success`, `failure` |
| `completed_at` | string | ISO 8601 completion timestamp |
| `result` | object | Detection results grouped by match type |

### Result Categories

| Category | Description |
| --- | --- |
| `signature` | Overall signature similarity matches |
| `vocal` | Vocal melody similarity matches |
| `inst` | Instrumental similarity matches |
| `topline` | Topline (main melody) similarity matches |

### Match Object Fields

| Field | Type | Description |
| --- | --- | --- |
| `signature_metric` | float | Overall similarity score (0.0 - 1.0) |
| `original` | object | Information about the query segment |
| `comparison` | object | Information about the matched segment |
| `scores` | object | Detailed similarity scores by component |

### Original / Comparison Fields

| Field | Type | Description |
| --- | --- | --- |
| `title` | string | Song title |
| `link` | string | Audio file URL (null for uploaded files) |
| `time_start` | float | Segment start time (seconds) |
| `time_end` | float | Segment end time (seconds) |
| `key` | string | Musical key (e.g., "G major", "E minor") |
| `chords` | array | Chord progression in shorthand notation (fixed length: 16 chords). Format: `Root:quality` (e.g., "C:maj", "E:min", "D:maj7"). "N" indicates no chord detected. |

### Score Object Fields

Each component (vocal, melody, topline) contains:

| Field | Type | Description |
| --- | --- | --- |
| `metric` | float | Final similarity metric for this component (0.0 - 1.0) |
| `pitch_score` | float | Pitch-based similarity score (0.0 - 1.0) |
| `correlation` | float | Rhythmic pattern correlation (0.0 - 1.0) |
| `ratio` | float | Matching ratio between segments (0.0 - 1.0) |
| `bpm_ratio` | float | Tempo similarity ratio (0.0 - 1.0) |
| `difficulty` | float | Analysis difficulty factor (0.0 - 1.0), higher values indicate more complex musical content, ex) simple rapping goes low difficulty. |

| Field | Type | Description |
| --- | --- | --- |
| `chord` | float | Chord progression similarity (0.0 - 1.0) |


## Notes

- **Segment-based**: Results show which specific parts of songs are similar. You will get 'simplified' results rather than mippia website.