# Error Handling

## HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid or missing API key |
| 422 | Validation Error - Request body validation failed |
| 429 | Rate Limit Exceeded |
| 500 | Internal Server Error |

## Error Response Format
```json
{
  "error": {
    "code": "invalid_request",
    "message": "The file_path parameter is required",
    "details": {
      "field": "file_path",
      "issue": "missing_required_field"
    }
  }
}
```

## Common Errors

### 401 Unauthorized

**Cause**: Missing or invalid API key

**Solution**: Check that you're including the correct API key in the `Authorization` header:
```bash
-H "Authorization: Bearer YOUR_API_KEY"
```

### 422 Validation Error

**Cause**: Invalid request parameters

**Solution**: Verify all required fields are present and properly formatted.

### 429 Rate Limit Exceeded

**Cause**: Too many requests in a short time period

**Solution**: Implement exponential backoff and respect rate limits. See [Rate Limits](../resources/rate-limits.md).

## Retry Logic

Implement exponential backoff for transient errors:
```python
import time
import random

def retry_with_backoff(func, max_retries=3):
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            if i == max_retries - 1:
                raise
            wait_time = (2 ** i) + random.random()
            time.sleep(wait_time)
```

:::{tip}
Only retry on 5xx errors and 429 (rate limit). Don't retry on 4xx errors (except 429).
:::