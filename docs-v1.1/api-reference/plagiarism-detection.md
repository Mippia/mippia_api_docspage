# Music Plagiarism Detection

Detect potential music plagiarism by comparing audio against a database of existing songs using structural music analysis.

## Endpoint

```
POST /api/v1/plagiarism/{model_name}
```

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|:-----|:-----|:---------|:------------|
| `model_name` | string | Yes | Model to use: `standard` |

### Request Body

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `file` | binary | Yes | Audio file to analyze (mp3, wav, flac, m4a, aac, ogg) |
| `dataset_id` | string | No | Dataset ID for comparison. `default` is only option available for now. |

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
|:------|:-----|:------------|
| `task_id` | string | Unique task identifier |
| `task_type` | string | Task type: `plagiarism_detection` |
| `status` | string | Task status: `pending`, `processing`, `success`, `failure` |
| `completed_at` | string | ISO 8601 completion timestamp |
| `result` | object | Detection results grouped by category |

### Result Categories

Results are grouped into four categories based on what aspect of the music matched:

| Category | Description |
|:---------|:------------|
| `signature` | Overall musical signature matches |
| `vocal` | Vocal melody matches |
| `inst` | Instrumental matches |
| `topline` | Main melody (topline) matches |

Each category contains an array of match objects.

### Match Object

| Field | Type | Description |
|:------|:-----|:------------|
| `signature_metric` | float | Overall similarity score (0.0 - 1.0) |
| `original` | object | Query segment info |
| `comparison` | object | Matched segment info |
| `scores` | object | Detailed scores by component |

### Segment Info (original / comparison)

| Field | Type | Description |
|:------|:-----|:------------|
| `title` | string | Song title |
| `link` | string | Audio URL (null for uploaded files) |
| `time_start` | float | Start time in seconds |
| `time_end` | float | End time in seconds |
| `key` | string | Musical key (e.g., "G major") |
| `chords` | array | 16 chords in shorthand notation (e.g., "C:maj", "E:min", "N" for none) |

### Scores

The `scores` object contains similarity breakdowns for `vocal`, `melody`, and `topline`:

| Field | Type | Description |
|:------|:-----|:------------|
| `metric` | float | Final similarity score (0.0 - 1.0) |
| `pitch_score` | float | Pitch similarity (0.0 - 1.0) |
| `correlation` | float | Rhythmic pattern similarity (0.0 - 1.0) |
| `ratio` | float | Segment matching ratio (0.0 - 1.0) |
| `bpm_ratio` | float | Tempo similarity (0.0 - 1.0) |
| `difficulty` | float | Content complexity (0.0 - 1.0). Simple patterns like rapping score lower. |

Additionally:

| Field | Type | Description |
|:------|:-----|:------------|
| `chord` | float | Chord progression similarity (0.0 - 1.0) |

## Notes

- **Segment-based**: Results show which specific parts of songs are similar. API returns simplified results compared to the MIPPIA website.