# Quick Setup Guide - Step by Step

This is a condensed setup guide. For detailed information, see [README.md](README.md).

## Quick Start (5-10 minutes setup + model download)

### 1. Create Environment (1 minute)

```bash
conda create -n f5tts_vn python=3.11 -y
conda activate f5tts_vn
```

### 2. Install FFmpeg (2-5 minutes)

**⚠️ This may take 2-5 minutes - you can run it in background**

```bash
conda install -c conda-forge ffmpeg -y
```

### 3. Install Python Packages (5-10 minutes)

**⚠️ This downloads packages - may take 5-10 minutes**

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. First Run - Model Download

**⚠️ First time will download models (~3-5GB, 10-30 minutes)**

On first run, the application will automatically download:
- F5-TTS Vietnamese model (~3GB)
- Vocoder model (~500MB)
- ASR model (~500MB)

**You can run the app and let it download in the background.** The app will show progress.

## Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| "Exec format error" | Already fixed in code - just restart |
| "TorchCodec required" | Run: `conda install -c conda-forge ffmpeg -y` |
| "Could not load libtorchcodec" | Run: `conda install -c conda-forge ffmpeg -y` |
| Slow first run | Normal - models downloading |
| Out of memory | Close other apps, use shorter audio clips |

## Commands Reference

```bash
# Activate environment
conda activate f5tts_vn

# Run app
python app.py

# Check FFmpeg
ffmpeg -version

# Deactivate environment
conda deactivate
```

## Time Estimates

| Step | Estimated Time |
|------|---------------|
| Environment creation | 1 minute |
| FFmpeg installation | 2-5 minutes |
| Python packages | 5-10 minutes |
| First model download | 10-30 minutes |
| Subsequent runs | Instant |

---

**Ready to use after Step 4!** Models download automatically on first use.

