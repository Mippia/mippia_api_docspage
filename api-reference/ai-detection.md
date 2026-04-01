# AI Music Detection 

Detect AI-generated music.

### Endpoint

| Method | URI | Description |
| :--- | :--- | :--- |
| POST | `/api/v1/ai-detection/{model_name}` | Detect AI-generated music |

### Path Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `model_name` | string | Yes | Model to use: `lite`, `standard`, `pro`, `pro-v2` |

### Request Body

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | binary | Yes | Audio file to analyze (mp3, wav, flac, m4a, aac, ogg) |

---

## Models

| Model | Processing Time | Description |
| :--- | :--- | :--- |
| `lite` | 30-40 seconds | Single model, fast detection |
| `standard` | 30-40 seconds | Model ensemble, balanced accuracy |
| `pro` | ~1 minute | Model ensemble with detailed classification |
| `pro-v2` | ~15 seconds | AI tracking with role-based detection |

---

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

## Callback Response (Completed - Pro-V2)

Pro-V2 model includes role-based AI detection with separate 2-label and 5-label classifiers:

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "status": "success",
  "model_type": "pro-v2",
  "completed_at": "2025-12-04T05:30:20Z",
  "result": {
    "audio_filename.mp3": {
      "final_result": {
        "prediction": "fake",
        "confidence": 0.8234
      },
      "model_results": [
        {
          "segment_analysis": {
            "prediction": ["real", "fake", "real", "fake"],
            "confidence": [0.912, 0.834, 0.901, 0.823]
          },
          "overall_analysis": {
            "prediction": "fake",
            "confidence": 0.8775
          },
          "config": {
            "model_id": "2label_stage1",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        },
        {
          "overall_analysis": {
            "prediction": "fake",
            "confidence": 0.8654
          },
          "config": {
            "model_id": "2label_stage2",
            "analysis_focus": "Waveform & Melody Pattern",
            "task": "Real/Fake Binary Classification",
            "num_classes": 2,
            "labels": ["real", "fake"]
          }
        },
        {
          "segment_analysis": {
            "prediction": [["tracker", "engineer"], ["topliner"], ["real"], ["vocalist", "tracker"]],
            "confidence": [
              {"real": 0.05, "tracker": 0.62, "topliner": 0.12, "lyricist": 0.08, "vocalist": 0.08, "engineer": 0.65},
              {"real": 0.10, "tracker": 0.15, "topliner": 0.78, "lyricist": 0.05, "vocalist": 0.12, "engineer": 0.10},
              {"real": 0.92, "tracker": 0.03, "topliner": 0.02, "lyricist": 0.01, "vocalist": 0.02, "engineer": 0.03},
              {"real": 0.08, "tracker": 0.71, "topliner": 0.05, "lyricist": 0.03, "vocalist": 0.56, "engineer": 0.12}
            ]
          },
          "overall_analysis": {
            "prediction": ["tracker", "topliner", "vocalist", "engineer"],
            "confidence": {
              "real": 0.06,
              "tracker": 0.62,
              "topliner": 0.48,
              "lyricist": 0.04,
              "vocalist": 0.45,
              "engineer": 0.58
            }
          },
          "config": {
            "model_id": "5label_stage1",
            "analysis_focus": "Role-based AI Detection",
            "task": "Multi-role AI Detection",
            "num_classes": 6,
            "labels": ["real", "tracker", "topliner", "lyricist", "vocalist", "engineer"]
          }
        },
        {
          "segment_analysis": {
            "prediction": [["tracker", "engineer"], ["topliner"], ["real"], ["vocalist", "tracker"]],
            "confidence": [
              {"real": 0.04, "tracker": 0.65, "topliner": 0.10, "lyricist": 0.07, "vocalist": 0.09, "engineer": 0.68},
              {"real": 0.09, "tracker": 0.14, "topliner": 0.80, "lyricist": 0.04, "vocalist": 0.11, "engineer": 0.09},
              {"real": 0.94, "tracker": 0.02, "topliner": 0.01, "lyricist": 0.01, "vocalist": 0.01, "engineer": 0.02},
              {"real": 0.07, "tracker": 0.73, "topliner": 0.04, "lyricist": 0.02, "vocalist": 0.59, "engineer": 0.13}
            ]
          },
          "overall_analysis": {
            "prediction": ["tracker", "topliner", "vocalist", "engineer"],
            "confidence": {
              "real": 0.04,
              "tracker": 0.64,
              "topliner": 0.50,
              "lyricist": 0.03,
              "vocalist": 0.47,
              "engineer": 0.60
            }
          },
          "config": {
            "model_id": "5label_stage2",
            "analysis_focus": "Role-based AI Detection",
            "task": "Multi-role AI Detection",
            "num_classes": 6,
            "labels": ["real", "tracker", "topliner", "lyricist", "vocalist", "engineer"]
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
| Role-based AI Detection | Analyzes AI involvement by musical role (tracking, toplining, lyrics, vocals, engineering) |

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
| Multi-role AI | `real`, `tracker`, `topliner`, `lyricist`, `vocalist`, `engineer` |

## Notes

- **Supported formats**: mp3, wav, flac, m4a, aac, ogg
- **Final Result**: Weighted average of all Real/Fake binary classification models for a single consolidated prediction
- **Segment Analysis**: Analyzes each segment of the audio independently to detect localized AI artifacts
- **Overall Analysis**: Considers the entire song structure and aggregates segment results for final prediction
- **Model Results**: Each element in the `model_results` array represents one model's analysis
- **Pro-V2 Role Detection**: The 5-label models detect AI involvement by musical role. For segment-level analysis, prediction is an array of arrays where each segment contains detected roles (or `["real"]` if no AI detected). Confidence provides per-role probabilities for each segment. At the overall level, prediction lists all detected roles, and confidence aggregates role probabilities across segments.
