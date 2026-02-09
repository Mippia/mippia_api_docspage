# Lyric Plagiarism Detection

Analyze semantic similarity between lyrics using multilingual text understanding.

## Endpoint

```
POST /api/v1/lyric-plagiarism/{model_name}
```

## Parameters

### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `model_name` | string | Yes | Model to use: `standard` only for now! |

### Request Body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `lyric_text` | string | Yes | Lyrics to analyze (sentences separated by `\n`) |
| `song_title` | string | Yes | Title of the song |

## Request Example

### cURL

```bash
curl https://platform.mippia.com/api/v1/lyric-plagiarism/standard \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "lyric_text": "I walk alone through empty streets\nSearching for a love I cannot find\nThe stars above remind me of your eyes\nBut you are gone and left me here behind",
    "song_title": "Empty Streets"
  }'
```

### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/lyric-plagiarism/standard"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "lyric_text": "I walk alone through empty streets\nSearching for a love I cannot find\nThe stars above remind me of your eyes\nBut you are gone and left me here behind",
    "song_title": "Empty Streets"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## Response (Initial)

```json
{
  "taskId": "string"
}
```

## Callback Response (Completed)

```json
{
  "task_id": "task_20251204052920_J8uNdq5z",
  "task_name": "lyric_plagiarism_checking",
  "status": "completed",
  "completed_at": "2025-12-04T05:29:28Z",
  "result": {
    "max_similarity": 0.7234,
    "total_songs_checked": 163706,
    "top_matches": [
      {
        "rank": 1,
        "artist": "Artist Name",
        "title": "Similar Song Title",
        "year": "2019",
        "combined_score": 0.7234,
        "paragraph_score": 0.6891,
        "sentence_score": 0.7234,
        "similar_parts": [
          {
            "query_sentence": "I walk alone through empty streets",
            "target_sentence": "Walking alone on lonely roads",
            "similarity": 0.8123
          },
          {
            "query_sentence": "The stars above remind me of your eyes",
            "target_sentence": "Your eyes shine like the stars at night",
            "similarity": 0.7856
          }
        ]
      },
      {
        "rank": 2,
        "artist": "Another Artist",
        "title": "Another Song",
        "year": "2021",
        "combined_score": 0.6542,
        "paragraph_score": 0.6542,
        "sentence_score": 0.5891,
        "similar_parts": [
          {
            "query_sentence": "Searching for a love I cannot find",
            "target_sentence": "Looking for a love that's hard to find",
            "similarity": 0.7654
          }
        ]
      }
    ]
  }
}
```

## Result Fields

| Field | Type | Description |
| --- | --- | --- |
| `max_similarity` | float | Highest similarity score (0.0 - 1.0) |
| `total_songs_checked` | integer | Number of songs in the database |
| `top_matches` | array | Top 20 most similar songs |
| `top_matches[].rank` | integer | Ranking position |
| `top_matches[].artist` | string | Artist name |
| `top_matches[].title` | string | Song title |
| `top_matches[].year` | string | Release year |
| `top_matches[].paragraph_score` | float | Full lyrics similarity |
| `top_matches[].sentence_score` | float | Best matching sentence similarity |
| `top_matches[].similar_parts` | array | Top 3 most similar sentence pairs |

## Notes

- **Sentence splitting**: Input lyrics are split into sentences by newline (`\n`). Each line is treated as a separate sentence for analysis.
- **Language support**: 100+ languages supported via multilingual embeddings
- **Processing time**: 5-10 seconds typical
- **Database**: 160,000+ songs indexed

> **Note**: This API is currently in Beta and is free to use. Pricing will be announced before general availability. Future Tasks : phonetic/rhyme similarity in lyrics! 