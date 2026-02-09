# Changelog

All notable changes to the MIPPIA API will be documented in this file.

---

## v1.1.1 (2026-02-09)

### Changed
- **Pre-upload system**: Audio files are now uploaded separately via `POST /api/v1/music`, which returns a `musicId`. All analysis endpoints (`ai-detection`, `plagiarism`, `lyric_transcription`) now accept `musicId` instead of direct file upload.
- **Upload Music API**: New endpoint `POST /api/v1/music` for uploading audio files before analysis.
- **Updated Quick Start**: Added upload step to the getting started guide.

### Migration from v1.1
- Replace direct file uploads (`-F "file=@audio.mp3"`) with a two-step process:
  1. Upload file: `POST /api/v1/music` → receive `musicId`
  2. Analyze: `POST /api/v1/{endpoint}` with `{"musicId": "..."}` in JSON body

---

## v1.1 (2026-02-03)

### Added
- **Lyric Transcription API**: `POST /api/v1/lyric_transcription/{model}` — Extract lyrics from audio files using AI-powered speech recognition.
  - 18 languages supported (Korean, English, Chinese, Japanese, Spanish, French, German, Italian, Portuguese, Arabic, Hindi, Thai, Vietnamese, Indonesian, Turkish, Polish, Dutch, Russian)
  - Instrumental track detection
  - Vocal separation using Demucs
  - Language probability detection

---

## v1.0 (2025-12-16)

### Added
- **AI Music Detection**: `POST /api/v1/ai-detection/{model_name}` — Detect AI-generated music with `lite`, `standard`, and `pro` models.
- **Music Plagiarism Detection**: `POST /api/v1/plagiarism/{model_name}` — Compare audio against existing song databases.
- **Lyric Plagiarism Analysis**: `POST /api/v1/lyric-plagiarism/{model_name}` — Semantic similarity analysis for lyrics (100+ languages).
- **Dataset Management**: Custom dataset creation for plagiarism detection.
- **Webhook Integration**: Real-time callback notifications with HMAC-SHA256 signature verification.
- **Documentation**: Getting started guide, authentication, pricing, rate limits, and support resources.
