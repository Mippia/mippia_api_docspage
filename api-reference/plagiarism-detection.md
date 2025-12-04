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
| `dataset_id` | string | Yes | Dataset ID for comparison |

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
        "signature_metric": 0.847,
        "original": {
          "title": "My New Song",
          "link": "https://example.com/my-song.mp3",
          "time_start": 30.5,
          "time_end": 45.2,
          "key": "C major",
          "chords": ["C", "Am", "F", "G", "C", "Am", "Dm", "G", "C", "F", "Am", "G", "F", "C", "G", "C"]
        },
        "comparison": {
          "title": "Similar Existing Song",
          "link": "https://example.com/existing-song.mp3",
          "time_start": 15.0,
          "time_end": 30.0,
          "key": "C major",
          "chords": ["C", "Am", "F", "G", "C", "Am", "Dm", "G", "C", "F", "Am", "G", "F", "C", "G", "C"]
        },
        "scores": {
          "vocal": 0.823,
          "melody": 0.891,
          "bass": 0.756,
          "chord": 0.912
        }
      }
    ],
    "vocal": [
      {
        "signature_metric": 0.792,
        "original": {
          "title": "My New Song",
          "link": "https://example.com/my-song.mp3",
          "time_start": 45.0,
          "time_end": 60.0,
          "key": "G major",
          "chords": ["G", "Em", "C", "D", "G", "Em", "Am", "D", "G", "C", "Em", "D", "C", "G", "D", "G"]
        },
        "comparison": {
          "title": "Another Song",
          "link": "https://example.com/another-song.mp3",
          "time_start": 20.0,
          "time_end": 35.0,
          "key": "G major",
          "chords": ["G", "Em", "C", "D", "G", "Em", "Am", "D", "G", "C", "Em", "D", "C", "G", "D", "G"]
        },
        "scores": {
          "vocal": 0.856,
          "melody": 0.734,
          "bass": 0.689,
          "chord": 0.878
        }
      }
    ],
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
| `link` | string | Audio file URL or path |
| `time_start` | float | Segment start time (seconds) |
| `time_end` | float | Segment end time (seconds) |
| `key` | string | Musical key (e.g., "C major", "A minor") |
| `chords` | array | Chord progression (fixed length: 16 chords) |

### Score Fields

| Field | Type | Description |
| --- | --- | --- |
| `vocal` | float | Vocal melody similarity (0.0 - 1.0) |
| `melody` | float | Instrumental melody similarity (0.0 - 1.0) |
| `chord` | float | Chord progression similarity (0.0 - 1.0) |

## Analysis Method

The plagiarism detection system analyzes music at a structural level:

1. **Segmentation**: Audio is divided into musical segments based on beat and bar detection
2. **Feature Extraction**: Each segment is analyzed for vocal melody, instrumental melody, bass line, and chord progression (16 chords per segment)
3. **Clustering**: Segments are matched against pre-indexed clusters for efficient search
4. **Comparison**: Matched candidates are compared in detail using multiple similarity metrics

## Notes

- **Database**: 150,000+ songs indexed
- **Processing time**: 30-60 seconds typical
- **Segment-based**: Results show which specific parts of songs are similar
- **Multi-dimensional**: Analyzes vocal, melody, bass, and chord independently
- **Chord resolution**: Fixed 16-chord sequence per segment for consistent comparison

> **Note**: This API is currently in Beta. Pricing will be announced before general availability.