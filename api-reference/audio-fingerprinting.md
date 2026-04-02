# Audio Fingerprinting

Identify duplicate or identical songs by comparing audio fingerprints against the FAISS index.

## Endpoints

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| POST | `/api/v1/fingerprint/add` | Register audio fingerprint to index |
| POST | `/api/v1/fingerprint/check` | Check if audio matches existing fingerprint |

---

## Add Fingerprint

Register an audio file's fingerprint to the FAISS index for future comparison.

```
POST /api/v1/fingerprint/add
```

### Request Body

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `musicId` | string | Yes | Unique music identifier, uploaded via `[POST] /api/v1/music` endpoint |

### Request Example

#### cURL

```bash
curl https://platform.mippia.com/api/v1/fingerprint/add \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"musicId": "YOUR_MUSIC_ID"}'
```

#### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/fingerprint/add"
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

### Response (Initial)

```json
{
  "taskId": "string"
}
```

### Callback Response (Success)

```json
{
  "task_id": "task_20260402055414_AbCdEfGh",
  "task_name": "add_audio_in_index",
  "status": "success",
  "completed_at": "2026-04-02T14:54:14.859289"
}
```

### Callback Response (Failure)

```json
{
  "task_id": "task_20260402055414_AbCdEfGh",
  "task_name": "add_audio_in_index",
  "status": "failure",
  "completed_at": "2026-04-02T14:54:14.859289",
  "error": "Error message describing what went wrong"
}
```

---

## Check Fingerprint

Check if an audio file matches any existing fingerprint in the index.

```
POST /api/v1/fingerprint/check
```

### Request Body

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `musicId` | string | Yes | Unique music identifier, uploaded via `[POST] /api/v1/music` endpoint |

### Request Example

#### cURL

```bash
curl https://platform.mippia.com/api/v1/fingerprint/check \
  -X POST \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"musicId": "YOUR_MUSIC_ID"}'
```

#### Python

```python
import requests

url = "https://platform.mippia.com/api/v1/fingerprint/check"
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

### Response (Initial)

```json
{
  "taskId": "string"
}
```

### Callback Response (Duplicate Found)

```json
{
  "task_id": "task_20260402055414_LmxwriSZ",
  "task_name": "check_is_same",
  "status": "success",
  "result": {
    "is_duplicate": true,
    "matched_music_id": "6d516670-e81b-49b5-a1f6-465407f84830",
    "matched_musicname": "v2인간극장 오프닝"
  },
  "completed_at": "2026-04-02T14:54:14.859289"
}
```

### Callback Response (No Match)

```json
{
  "task_id": "task_20260402055414_LmxwriSZ",
  "task_name": "check_is_same",
  "status": "success",
  "result": {
    "is_duplicate": false,
    "matched_music_id": null,
    "matched_musicname": null
  },
  "completed_at": "2026-04-02T14:54:14.859289"
}
```

### Callback Response (Failure)

```json
{
  "task_id": "task_20260402055414_LmxwriSZ",
  "task_name": "check_is_same",
  "status": "failure",
  "completed_at": "2026-04-02T14:54:14.859289",
  "error": "Error message describing what went wrong"
}
```

---

## Result Fields

### Common Fields

| Field | Type | Description |
|:------|:-----|:------------|
| `task_id` | string | Unique task identifier |
| `task_name` | string | `add_audio_in_index` or `check_is_same` |
| `status` | string | Task status: `pending`, `processing`, `success`, `failure` |
| `completed_at` | string | ISO 8601 completion timestamp |
| `error` | string | Error message (only present when `status` is `failure`) |

### Check Result Fields

| Field | Type | Description |
|:------|:-----|:------------|
| `is_duplicate` | boolean | `true` if a matching fingerprint was found |
| `matched_music_id` | string \| null | Music ID of the matched song (`null` if no match) |
| `matched_musicname` | string \| null | Name of the matched song (`null` if no match) |

## Error Responses

| Status Code | Description |
|:------------|:------------|
| 401 | API key has expired |
| 404 | API key does not exist |
| 422 | Validation error (invalid request body) |
| 429 | Rate limit exceeded |

## Notes

- **Index registration required**: Before using `/fingerprint/check`, target songs must be registered via `/fingerprint/add`
- **Async processing**: Both endpoints return a `taskId` immediately. Results are delivered via [webhook callback](../guides/webhooks.md)
