# Dataset Management

Create and manage custom datasets for plagiarism detection.

## Dataset Creation

Create a new dataset with your music collection. 
```
POST /v1/dataset
```

:::{note}
This endpoint is currently in development. Contact [mippia@mippia.com](mailto:support@mippia.com) for beta access.
:::

## Dataset Add

Add tracks to an existing dataset.
```
POST /v1/dataset/{:dataset_id}/music
```

:::{note}
This endpoint is currently in development. Contact [mippia@mippia.com](mailto:support@mippia.com) for beta access.
:::

## Pricing

- **Free tier**: Up to 1,000 tracks per dataset
- **Processing time**: ~2 minutes per track
- **Enterprise**: For datasets exceeding 1,000 tracks, contact [mippia@mippia.com](mailto:enterprise@mippia.com)

## Use Cases

- Build reference libraries for specific genres or catalogs
- Maintain proprietary music databases
- Create custom plagiarism detection workflows
- Manage large-scale music collections