# Rate Limits

## Limits by Tier

| Tier | Requests/Minute | Daily Limit |
|------|-----------------|-------------|
| Free | 5 | 100 |
| Starter | 20 | 1,000 |
| Professional | 60 | 10,000 |
| Enterprise | Custom | Custom |

## Rate Limit Headers

All API responses include rate limit information:
```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1699564800
```

### Header Descriptions

- `X-RateLimit-Limit`: Maximum requests allowed in the current window
- `X-RateLimit-Remaining`: Requests remaining in the current window
- `X-RateLimit-Reset`: Unix timestamp when the limit resets

## Handling Rate Limits

### Check Headers

Always check rate limit headers before making requests:
```python
response = requests.get(url, headers=headers)
remaining = int(response.headers.get('X-RateLimit-Remaining', 0))

if remaining < 10:
    print("Warning: Approaching rate limit")
```

### Implement Backoff

When you hit a rate limit (429 status), implement exponential backoff:
```python
def make_request_with_backoff(url, max_retries=3):
    for i in range(max_retries):
        response = requests.get(url)
        
        if response.status_code != 429:
            return response
            
        retry_after = int(response.headers.get('Retry-After', 2 ** i))
        time.sleep(retry_after)
    
    raise Exception("Max retries exceeded")
```

## Best Practices

- Monitor rate limit headers
- Implement request queuing for high volumes
- Distribute requests evenly over time
- Use webhooks instead of polling
- Consider upgrading your tier if you regularly hit limits

:::{note}
Enterprise customers can request custom rate limits. Contact [mippia@mippia.com](mailto:mippia@mippia.com).
:::