# Git Push Guide - Staged Commits

This guide documents what has been pushed and what remains to be pushed.

## ✅ Stage 1: Basic Files (COMPLETED)

**Status**: ✅ Pushed to GitHub

**What was pushed**:
- All Python source code files (`.py`)
- Configuration files (`.yaml`)
- Documentation (`.md`, `.txt`)
- `requirements.txt`
- `.gitignore`
- Example files (small audio files < 500KB)
- Scripts and utilities

**Total**: ~1.35 MB (347 objects)

**Commands used**:
```bash
git add .gitignore README.md SETUP_GUIDE.md app.py requirements.txt
git add f5_tts/**/*.py f5_tts/**/*.yaml f5_tts/**/*.md
git commit -m "Add Mac compatibility fixes and documentation"
git push origin main
```

## 📦 Stage 2: Additional Files (If Needed)

If there are any missing code files or documentation, add them with:

```bash
# Check what's not tracked
git status

# Add specific files
git add <file_path>

# Commit
git commit -m "Add additional files"

# Push
git push origin main
```

## 🚫 Stage 3: Model Files (NOT YET PUSHED - Large Files)

**Status**: ❌ Not pushed (excluded via .gitignore)

**Why**: Model files are large (3GB+) and should be handled separately using:
1. **Git LFS** (Git Large File Storage) - Recommended for large files
2. **Separate repository** - For very large files
3. **External hosting** - Models are downloaded from Hugging Face automatically

**Files excluded**:
- `*.pt`, `*.pth`, `*.ckpt` (PyTorch model checkpoints)
- `*.bin`, `*.safetensors` (Model weights)
- `*.onnx` (ONNX models)
- Large audio files (`*.wav`, `*.flac`, `*.mp3` > 1MB)

**Current setup**: Models are automatically downloaded from Hugging Face on first run, so model files don't need to be in the repo.

## 🔍 Checking Repository Status

```bash
# See what's tracked
git ls-files

# See what's not tracked
git status

# Check repository size
du -sh .git
```

## 📝 Next Steps (If Needed)

### Option 1: Push Remaining Small Files

If there are any small code/config files still untracked:

```bash
# Review untracked files
git status

# Add and commit
git add <files>
git commit -m "Add remaining configuration files"
git push origin main
```

### Option 2: Set Up Git LFS for Large Files (If Models Needed)

```bash
# Install Git LFS (if not installed)
git lfs install

# Track large files
git lfs track "*.pt"
git lfs track "*.pth"
git lfs track "*.bin"

# Add .gitattributes
git add .gitattributes

# Commit
git commit -m "Add Git LFS tracking for large files"
git push origin main
```

**Note**: Git LFS requires a GitHub account with LFS quota. Free tier has 1GB storage + 1GB bandwidth/month.

## ✅ Current Status

- ✅ All source code: Pushed
- ✅ Documentation: Pushed
- ✅ Configuration files: Pushed
- ✅ Basic setup files: Pushed
- ❌ Model files: Excluded (auto-downloaded from Hugging Face)

## 🎯 Repository is Ready

The repository is **ready to use**. Models will be automatically downloaded from Hugging Face when users run the application for the first time.

**Repository URL**: https://github.com/thomasvuong/F5-TTS-Vietnamese_Clone_Voice_RunOnMac

---

**Last Updated**: After Stage 1 push completion

