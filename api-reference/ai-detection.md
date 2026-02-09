# AI Music Detection 

Detect AI-generated music.

### Endpoint

| Method | URI | Description |
| :--- | :--- | :--- |
| POST | `/api/v1/ai-detection/{model_name}` | Detect AI-generated music |

### Path Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `model_name` | string | Yes | Model to use: `lite`, `standard`, `pro` |

### Request Body

| Field      | Type | Required | Description |
|:-----------| :--- | :--- | :--- |
| `musicId` | string   | Unique music identifier      | uploaded via `[POST] /api/v1/music` endpoint |

---

## Models

| Model | Processing Time | Description |
| :--- | :--- | :--- |
| `lite` | 30-40 seconds | Single model, fast detection |
| `standard` | 30-40 seconds | Model ensemble, balanced accuracy |
| `pro` | ~1 minute | Model ensemble with detailed classification |

---

## Request Example

### cURL

```bash
curl https://platform.aippim.shop/api/v1/ai-detection/standard \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"musicId": "YOUR_MUSIC_ID"}'
```

### Python

```python
import requests

url = "https://platform.aippim.shop/api/v1/ai-detection/standard"
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
  "status": "processing",
  "result": null,
  "model_type": "standard"
}
```

## Callback Response (Completed - Standard)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "status": "success",
  "model_type": "standard",
  "completed_at": "2025-12-04T05:30:15Z",
  "result": {
    "audio_filename.mp3": {
      "final_result": {
        "prediction": "real",
        "confidence": 0.9382
      },
      "model_results": [
        {
          "overall_analysis": {
            "prediction": "real",
            "confidence": 0.923
          },
          "config": {
            "model_id": "model_0",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        },
        {
          "segment_analysis": {
            "prediction": ["real", "real", "real", "real"],
            "confidence": [0.891, 0.912, 0.887, 0.903]
          },
          "overall_analysis": {
            "prediction": "real",
            "confidence": 0.945
          },
          "config": {
            "model_id": "model_1",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        },
        {
          "segment_analysis": {
            "prediction": ["real", "real", "real", "real"],
            "confidence": [0.876, 0.901, 0.889, 0.912]
          },
          "overall_analysis": {
            "prediction": "real",
            "confidence": 0.934
          },
          "config": {
            "model_id": "model_2",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        },
        {
          "segment_analysis": {
            "prediction": ["real", "real", "real", "real"],
            "confidence": [0.902, 0.918, 0.895, 0.921]
          },
          "overall_analysis": {
            "prediction": "real",
            "confidence": 0.951
          },
          "config": {
            "model_id": "model_3",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        }
      ]
    }
  }
}
```

## Callback Response (Completed - Pro)

Pro model includes additional classifiers for detailed analysis:

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "status": "success",
  "model_type": "pro",
  "completed_at": "2025-12-04T05:30:45Z",
  "result": {
    "audio_filename.mp3": {
      "final_result": {
        "prediction": "fake",
        "confidence": 0.8654
      },
      "model_results": [
        {
          "overall_analysis": {
            "prediction": "fake",
            "confidence": 0.876
          },
          "config": {
            "model_id": "model_0",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        },
        {
          "segment_analysis": {
            "prediction": ["fake", "fake", "ai_cover", "fake"],
            "confidence": [0.712, 0.834, 0.623, 0.789]
          },
          "overall_analysis": {
            "prediction": "fake",
            "confidence": 0.823
          },
          "config": {
            "model_id": "model_4",
            "analysis_focus": "Mixing & Audio Effects",
            "task": "Real/AI-Cover/Fake 3-Class",
            "num_classes": 3,
            "labels": ["real", "ai_cover", "fake"]
          }
        },
        {
          "segment_analysis": {
            "prediction": ["suno_v4", "suno_v4", "suno_v4_5", "suno_v4"],
            "confidence": [0.534, 0.612, 0.489, 0.567]
          },
          "overall_analysis": {
            "prediction": "suno_v4",
            "confidence": 0.634
          },
          "config": {
            "model_id": "model_5",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Detailed Fake Source Classification",
            "num_classes": 6,
            "labels": ["real", "suno_v4", "suno_v4_5", "suno_v4_5_plus", "suno_v5", "other"]
          }
        },
        {
          "segment_analysis": {
            "prediction": ["fake", "fake", "fake", "fake"],
            "confidence": [0.891, 0.912, 0.878, 0.901]
          },
          "overall_analysis": {
            "prediction": "fake",
            "confidence": 0.912
          },
          "config": {
            "model_id": "model_6",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/AI-Cover/Fake 3-Class",
            "num_classes": 3,
            "labels": ["real", "ai_cover", "fake"]
          }
        }
      ]
    }
  }
}
```

## Result Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `task_id` | string | Unique task identifier |
| `status` | string | Task status: `pending`, `processing`, `success`, `failure` |
| `model_type` | string | Model used for detection |
| `completed_at` | string | ISO 8601 completion timestamp |
| `result` | object | Detection results keyed by filename |

### Result Structure

The result is an object where:
- **Key**: Audio filename
- **Value**: Object containing `final_result` and `model_results`

| Field | Type | Description |
| :--- | :--- | :--- |
| `final_result` | object | Aggregated prediction from all Real/Fake binary classification models |
| `model_results` | array | Individual results from each model in the ensemble |

### Final Result Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `prediction` | string | Final aggregated prediction: `real` or `fake` |
| `confidence` | float | Final confidence score (0.0 - 1.0) |

### Model Result Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `segment_analysis` | object | Results from analyzing individual segments (optional) |
| `overall_analysis` | object | Final prediction for the entire audio |
| `config` | object | Model configuration and metadata |

### Config Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `model_id` | string | Unique model identifier (e.g., `model_0`, `model_1`) |
| `analysis_focus` | string | What the model analyzes (see Analysis Focus below) |
| `task` | string | Classification task type |
| `num_classes` | integer | Number of output classes |
| `labels` | array | Possible prediction labels |

### Analysis Focus

| Focus | Description |
| :--- | :--- |
| Waveform & Melody Pattern | Analyzes audio waveform characteristics and melodic patterns |
| Mixing & Audio Effects | Analyzes mixing techniques and audio effect signatures |

### Analysis Result Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `segment_analysis` | object | Results from analyzing individual segments of the audio |
| `segment_analysis.prediction` | array | Prediction for each audio segment |
| `segment_analysis.confidence` | array | Confidence score for each segment |
| `overall_analysis` | object | Final prediction considering the entire song structure |
| `overall_analysis.prediction` | string | Final aggregated prediction |
| `overall_analysis.confidence` | float | Final confidence score (0.0 - 1.0) |

### Classification Labels

| Task | Labels |
| :--- | :--- |
| Real/Fake Binary | `real`, `fake` |
| 3-Class | `real`, `ai_cover`, `fake` |
| Detailed Fake Source | `real`, `suno_v4`, `suno_v4_5`, `suno_v4_5_plus`, `suno_v5`, `other` |

## Notes

- **Supported formats**: mp3, wav, flac, m4a, aac, ogg
- **Final Result**: Weighted average of all Real/Fake binary classification models for a single consolidated prediction
- **Segment Analysis**: Analyzes each segment of the audio independently to detect localized AI artifacts
- **Overall Analysis**: Considers the entire song structure and aggregates segment results for final prediction
- **Model Results**: Each element in the `model_results` array represents one model's analysis