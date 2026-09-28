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
| `musicId` | string   | Unique music identifier      | uploaded via `[POST] /api/v1/music` endpoint |
| `dataset_id` | string | No | Dataset ID for comparison. `default` is only option available for now. |

## Request Example
### cURL

```bash
curl https://platform.mippia.com/api/v1/plagiarism/standard \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"musicId": "YOUR_MUSIC_ID"}'
```

### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/plagiarism/standard"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "musicId": "YOUR_MUSIC_ID"
}

response = requests.post(url, headers=headers, json=data)
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
    "topline": [...],
    "total_scores": {
      "overall_score": 56.247343,
      "matched_title": "Similar Existing Song",
      "matched_category": "topline",
      "by_category": {
        "signature": [
          {
            "rank": 1,
            "title": "Similar Existing Song",
            "link": "https://www.youtube.com/watch?v=example",
            "scores": {
              "overall_score": 54.684332,
              "rhythm": 54.671,
              "instruments": {
                "vocal":   { "overall_metric": 55.68, "pitch_score": 77.33, "correlation": 54.67, "ratio": 96.38 },
                "inst":    { "overall_metric": 0.0,   "pitch_score": 43.63, "correlation": 8.81,  "ratio": 88.38 },
                "topline": { "overall_metric": 67.15, "pitch_score": 98.67, "correlation": 40.93, "ratio": 89.35 },
                "bass":    { "overall_metric": 0.0,   "pitch_score": 0.0,   "correlation": 0.0,   "ratio": 0.0 }
              },
              "chord": {
                "roman_numeral_similarity": 17.7,
                "quality_similarity": 17.7,
                "alteration_similarity": 17.7,
                "bass_similarity": 17.7,
                "overall_similarity": 17.7,
                "sequence_length": 17.7
              }
            }
          }
        ],
        "vocal": [...],
        "inst": [...],
        "topline": [...]
      }
    }
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
| `result` | object | Detection results: four segment-level categories plus `total_scores` |

### Result Categories

`result` contains four segment-level categories and one song-level summary (`total_scores`).
The segment categories show *which parts* matched; `total_scores` gives the *overall
percentage per reference track*, identical to the number shown on the MIPPIA website.

Segment categories, based on what aspect of the music matched:

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

### Total Scores (`total_scores`)

`total_scores` is the song-level summary. It is computed by the same function the
MIPPIA website uses, so the numbers match the website exactly. Use `overall_score`
when you need a single percentage per track (for example in a review dashboard).

| Field | Type | Description |
|:------|:-----|:------------|
| `overall_score` | float | Overall similarity percentage (0 - 99). Same value shown on the MIPPIA website. Equals the highest reference-track score across all categories. |
| `matched_title` | string | Reference track that produced `overall_score` |
| `matched_category` | string | Category of that match: `signature`, `vocal`, `inst`, or `topline` |
| `by_category` | object | Per-category arrays of reference tracks (up to 10 each), sorted by `scores.overall_score` descending |

#### Reference Track Object (`by_category.<category>[]`)

| Field | Type | Description |
|:------|:-----|:------------|
| `rank` | integer | Rank within the category (1 = most similar) |
| `title` | string | Reference track title |
| `link` | string | Reference track URL (may be null) |
| `scores` | object | Song-level score breakdown (see below) |

#### Song-level Scores (`scores`)

All values in this object are percentages (0 - 99).

| Field | Type | Description |
|:------|:-----|:------------|
| `overall_score` | float | Overall similarity for this reference track |
| `rhythm` | float | Rhythmic similarity |
| `instruments` | object | Per-instrument breakdown for `vocal`, `inst`, `topline`, `bass` |
| `instruments.<inst>.overall_metric` | float | Final similarity for that instrument |
| `instruments.<inst>.pitch_score` | float | Pitch similarity |
| `instruments.<inst>.correlation` | float | Rhythmic pattern similarity |
| `instruments.<inst>.ratio` | float | Segment matching ratio |
| `chord` | object | Chord-progression similarity: `roman_numeral_similarity`, `quality_similarity`, `alteration_similarity`, `bass_similarity`, `overall_similarity`, `sequence_length` |

#### Recommended thresholds

| `overall_score` | Recommendation |
|:----------------|:---------------|
| Above 50 | Needs review |
| Above 60 | High risk |

These are guidelines. Choose the values that fit your own review workflow.

## Notes

- **Segment-based**: The `signature`, `vocal`, `inst`, and `topline` arrays show which specific parts of songs are similar.
- **Song-level**: `total_scores` provides the overall percentage per reference track, matching the MIPPIA website. The segment-level fields alone cannot reproduce it, because the website applies internal normalization before aggregation.