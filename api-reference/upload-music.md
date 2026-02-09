# Upload audiofile

Upload an audio file to inspect

### Endpoint

| Method | URI             | Description |
| :--- |:----------------| :--- |
| POST | `/api/v1/music` | Upload an audio file to inspect|

### Request Body

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | binary | Yes | Audio file to inspect (mp3, wav, flac, m4a, aac, ogg) |

---

## Request Example

### cURL

```bash
curl https://platform.mippia.com/api/v1/music \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -X POST \
  -F "file=@/path/to/audio.mp3"
```

### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/music"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
files = {
    "file": open("/path/to/audio.mp3", "rb")
}

response = requests.post(url, headers=headers, files=files)
print(response.json())
```

## Response

| Field | Type     | Description                  |
| :--- |:---------|:-----------------------------|
| `musicId` | string   | Unique music identifier      |
| `title` | string   | filename                     |
| `created_at` | string | ISO 8601 timestamp of upload |

```json
{
  "musicId": "MUSIC-UUID",
  "title": "audio",
  "created_at": "2025-12-04T05:29:20Z"
}
```