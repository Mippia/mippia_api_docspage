# Rate Limits

## Limits by Tier

| Tier | Requests/Minute |
|------|-----------------|
| Free | 10 | 
| Paid(Standard / Premium CUD) | 100 | 
| Enterprise | Custom | Custom |





## Best Practices

- Monitor rate limit headers
- Implement request queuing for high volumes
- Distribute requests evenly over time
- Use webhooks instead of polling
- Consider upgrading your tier if you regularly hit limits

:::{note}
Enterprise customers can request custom rate limits. Contact [mippia@mippia.com](mailto:mippia@mippia.com).
:::