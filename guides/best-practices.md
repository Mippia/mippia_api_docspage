# Best Practices

## Async Request Handling

All MIPPIA APIs work asynchronously:

1. Submit your request and receive a `task_id`
2. Set up webhooks or poll the status endpoint
3. Retrieve results when status is `completed`

:::{tip}
**Use webhooks instead of polling** to reduce unnecessary API calls and get results immediately.
:::

## File Formats

### Supported Formats

- MP3
- WAV
- FLAC
- M4A
- OGG

### Recommendations

- Use high-quality audio (320kbps or higher)
- Ensure files are properly encoded
- Keep file sizes under 50MB
- Use lossless formats (FLAC, WAV) for best accuracy

## Error Handling

Always implement proper error handling:
```python
import requests

def analyze_track(file_path):
    try:
        response = requests.post(
            "https://api.mippia.com/v1/models/ai-detection-standard",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"file_path": file_path, "filename": "track.mp3"}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code}")
        print(f"Details: {e.response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
```

## Rate Limiting

- Monitor your usage in the dashboard
- Implement request queuing for high-volume processing
- Use appropriate tiers for your use case
- Cache results when possible

## Security

- **Never expose API keys** in client-side code
- Use environment variables for API keys
- Rotate keys periodically
- Set up webhook signature verification
- Use HTTPS for all requests

## Performance Optimization

### Choose the Right Model

- **Lite**: Use for initial screening or high-volume processing
- **Standard**: Default choice for most use cases
- **Pro**: Use only when detailed analysis is required

### Batch Processing

For multiple files, submit them concurrently but respect rate limits:
```python
import asyncio
import aiohttp

async def process_batch(file_paths):
    async with aiohttp.ClientSession() as session:
        tasks = [analyze_track_async(session, fp) for fp in file_paths]
        return await asyncio.gather(*tasks)
```

## Cost Optimization

- Use Lite model for initial screening
- Upgrade to Standard/Pro only for flagged content
- Cache results to avoid duplicate analysis
- Monitor usage and set budget alerts
- Consider Enterprise pricing for high volumes (10,000+ requests/month)