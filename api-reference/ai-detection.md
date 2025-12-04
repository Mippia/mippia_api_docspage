# AI Music Detection

Detect AI-generated music using ensemble deep learning models.

## Endpoint

```
POST /api/v1/ai-detection/{model_name}
```

## Parameters

### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model_name` | string | Yes | Model to use: `lite`, `standard`, `pro` |

### Request Body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | binary | Yes | Audio file to analyze (mp3, wav, flac, m4a, aac, ogg) |

## Models

| Model | Processing Time | Price | Description |
| --- | --- | --- | --- |
| `lite` | 10-20 seconds | $0.10 | Single model, fast detection |
| `standard` | ~1 minute | $0.20 | 4-model ensemble, balanced accuracy |
| `pro` | ~1 minute | $0.50 | 7-model ensemble with detailed classification |

## Request Example

### cURL

```bash
curl https://platform.mippia.com/api/v1/ai-detection/standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -X POST \
  -F "file=@/path/to/audio.mp3"
```

### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/ai-detection/standard"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
files = {
    "file": open("/path/to/audio.mp3", "rb")
}

response = requests.post(url, headers=headers, files=files)
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
      "model_0": {
        "overall_analysis": {
          "prediction": "real",
          "confidence": 0.923
        }
      },
      "model_0_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Real/Fake Binary Classification",
        "num_classes": 2,
        "labels": ["real", "fake"]
      },
      "model_1": {
        "segment_analysis": {
          "prediction": ["real", "real", "real", "real"],
          "confidence": [0.891, 0.912, 0.887, 0.903]
        },
        "overall_analysis": {
          "prediction": "real",
          "confidence": 0.945
        }
      },
      "model_1_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Real/Fake Binary Classification",
        "num_classes": 2,
        "labels": ["real", "fake"]
      },
      "model_2": {
        "segment_analysis": {
          "prediction": ["real", "real", "real", "real"],
          "confidence": [0.876, 0.901, 0.889, 0.912]
        },
        "overall_analysis": {
          "prediction": "real",
          "confidence": 0.934
        }
      },
      "model_2_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Real/Fake Binary Classification",
        "num_classes": 2,
        "labels": ["real", "fake"]
      },
      "model_3": {
        "segment_analysis": {
          "prediction": ["real", "real", "real", "real"],
          "confidence": [0.902, 0.918, 0.895, 0.921]
        },
        "overall_analysis": {
          "prediction": "real",
          "confidence": 0.951
        }
      },
      "model_3_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Real/Fake Binary Classification",
        "num_classes": 2,
        "labels": ["real", "fake"]
      }
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
      "model_0": {
        "overall_analysis": {
          "prediction": "fake",
          "confidence": 0.876
        }
      },
      "model_0_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Real/Fake Binary Classification",
        "num_classes": 2,
        "labels": ["real", "fake"]
      },
      "model_4": {
        "segment_analysis": {
          "prediction": ["fake", "fake", "ai_cover", "fake"],
          "confidence": [0.712, 0.834, 0.623, 0.789]
        },
        "overall_analysis": {
          "prediction": "fake",
          "confidence": 0.823
        }
      },
      "model_4_config": {
        "analysis_focus": "Mixing & Audio Effects",
        "task": "Real/AI-Cover/Fake 3-Class",
        "num_classes": 3,
        "labels": ["real", "ai_cover", "fake"]
      },
      "model_5": {
        "segment_analysis": {
          "prediction": ["suno_v4", "suno_v4", "suno_v4_5", "suno_v4"],
          "confidence": [0.534, 0.612, 0.489, 0.567]
        },
        "overall_analysis": {
          "prediction": "suno_v4",
          "confidence": 0.634
        }
      },
      "model_5_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Detailed Fake Source Classification",
        "num_classes": 6,
        "labels": ["real", "suno_v4", "suno_v4_5", "suno_v4_5_plus", "suno_v5", "suno_other"]
      },
      "model_6": {
        "segment_analysis": {
          "prediction": ["fake", "fake", "fake", "fake"],
          "confidence": [0.891, 0.912, 0.878, 0.901]
        },
        "overall_analysis": {
          "prediction": "fake",
          "confidence": 0.912
        }
      },
      "model_6_config": {
        "analysis_focus": "Waveform & Melody Pattern",
        "task": "Real/AI-Cover/Fake 3-Class",
        "num_classes": 3,
        "labels": ["real", "ai_cover", "fake"]
      }
    }
  }
}
```

## Result Fields

| Field | Type | Description |
| --- | --- | --- |
| `task_id` | string | Unique task identifier |
| `status` | string | Task status: `pending`, `processing`, `success`, `failure` |
| `model_type` | string | Model used for detection |
| `completed_at` | string | ISO 8601 completion timestamp |
| `result` | object | Detection results keyed by filename |

### Model Result Fields

| Field | Type | Description |
| --- | --- | --- |
| `model_N` | object | Individual model result (N = 0, 1, 2, ...) |
| `model_N_config` | object | Model configuration and metadata |

### Model Config Fields

| Field | Type | Description |
| --- | --- | --- |
| `analysis_focus` | string | What the model analyzes (see Analysis Focus below) |
| `task` | string | Classification task type |
| `num_classes` | integer | Number of output classes |
| `labels` | array | Possible prediction labels |

### Analysis Focus

| Focus | Description |
| --- | --- |
| Waveform & Melody Pattern | Analyzes audio waveform characteristics and melodic patterns |
| Mixing & Audio Effects | Analyzes mixing techniques and audio effect signatures |

### Analysis Result Fields

| Field | Type | Description |
| --- | --- | --- |
| `segment_analysis` | object | Results from analyzing individual segments of the audio |
| `segment_analysis.prediction` | array | Prediction for each audio segment |
| `segment_analysis.confidence` | array | Confidence score for each segment |
| `overall_analysis` | object | Final prediction considering the entire song structure |
| `overall_analysis.prediction` | string | Final aggregated prediction |
| `overall_analysis.confidence` | float | Final confidence score (0.0 - 1.0) |

### Classification Labels

| Task | Labels |
| --- | --- |
| Real/Fake Binary | `real`, `fake` |
| 3-Class | `real`, `ai_cover`, `fake` |
| Detailed Fake Source | `real`, `suno_v4`, `suno_v4_5`, `suno_v4_5_plus`, `suno_v5`, `other` |

## Notes

- **Supported formats**: mp3, wav, flac, m4a, aac, ogg
- **Segment Analysis**: Analyzes each segment of the audio independently to detect localized AI artifacts
- **Overall Analysis**: Considers the entire song structure and aggregates segment results for final prediction

> **Note**: This API is currently in Beta. Pricing may change before general availability.