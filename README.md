# F5-TTS Vietnamese Clone Voice - Mac Setup Guide

A text-to-speech system for Vietnamese voice cloning, optimized for macOS (Apple Silicon). This repository includes fixes for running F5-TTS on Mac with proper dependencies and error handling.

## 🎯 Features

- Vietnamese voice cloning using F5-TTS
- Web-based interface using Gradio
- Optimized for macOS (Apple Silicon M1/M2/M3)
- Automatic fallback for audio loading issues
- Reference audio transcription support

## 📋 Prerequisites

- macOS (tested on Apple Silicon)
- Miniconda or Anaconda installed
- Python 3.11

## 🚀 Installation Guide

### Step 1: Create and Activate Conda Environment

```bash
# Create conda environment
conda create -n f5tts_vn python=3.11 -y

# Activate environment
conda activate f5tts_vn
```

### Step 2: Install System Dependencies

Install FFmpeg (required for torchcodec):

```bash
conda install -c conda-forge ffmpeg -y
```

**Note:** This command may take 2-5 minutes as it installs FFmpeg and many dependencies (74MB+). Run it in a separate terminal if needed.

### Step 3: Install Python Dependencies

```bash
# Install from requirements.txt
pip install -r requirements.txt
```

**Note:** Installing all packages may take 5-10 minutes. The model files will be downloaded automatically on first run (3GB+ for the Vietnamese model).

### Step 4: Verify Installation

```bash
# Check FFmpeg
ffmpeg -version

# Check Python packages
python -c "import torch; import torchaudio; import gradio; print('All packages installed successfully!')"
```

## 🏃 Running the Application

### Start the Web Interface

```bash
# Make sure you're in the conda environment
conda activate f5tts_vn

# Run the application
python app.py
```

The application will start and provide a local URL (typically `http://127.0.0.1:7860`). Open it in your browser.

### Usage

1. **Upload Reference Audio**: Upload a sample voice file (recommended: 5-15 seconds, clear speech)
2. **Enter Text**: Type the Vietnamese text you want to generate
3. **Adjust Speed** (optional): Use the slider to adjust speech speed (0.3x - 2.0x)
4. **Generate**: Click "Generate Voice" to create the cloned voice

## 🔧 Troubleshooting

### Error: "Exec format error" with vinorm

**Solution**: This is fixed! The code now automatically falls back to using the original text if Vietnamese normalization fails on Apple Silicon.

### Error: "TorchCodec is required"

**Solution**: This is fixed! The code includes:
1. FFmpeg installation (see Step 2 above)
2. Automatic fallback to `soundfile` if torchcodec fails

### Error: "Could not load libtorchcodec"

**Solution**: 
1. Ensure FFmpeg is installed: `conda install -c conda-forge ffmpeg -y`
2. If issues persist, the code will automatically fall back to alternative audio loading methods

### Slow Performance on Mac

- The model runs on MPS (Metal Performance Shaders) for Apple Silicon
- First run will be slower as models are downloaded and cached
- For faster inference, consider using shorter reference audio clips (under 10 seconds)

## 📁 Project Structure

```
F5-TTS-Vietnamese-100h/
├── app.py                      # Main Gradio application
├── requirements.txt            # Python dependencies
├── f5_tts/
│   ├── infer/
│   │   └── utils_infer.py     # Inference utilities (with Mac fixes)
│   ├── model/                  # Model definitions
│   ├── configs/                # Training configurations
│   └── ...
└── README.md                   # This file
```

## 🔑 Key Fixes for Mac Compatibility

1. **Vietnamese Text Normalization**: Added fallback when `vinorm` fails on Apple Silicon
2. **Audio Loading**: Added `load_audio_with_fallback()` function that tries `torchaudio` first, then falls back to `soundfile`
3. **ASR Pipeline**: Modified transcription to preload audio and pass as numpy array to avoid torchcodec issues
4. **FFmpeg Support**: Added FFmpeg installation to support torchcodec

## 📝 Important Notes

### Model Files

Model files are automatically downloaded from Hugging Face on first run:
- Model: `hf://hynt/F5-TTS-Vietnamese-ViVoice/model_last.pt` (~3GB)
- Vocoder: `charactr/vocos-mel-24khz`
- ASR: `vinai/PhoWhisper-medium`

**Note**: First run will download ~3-5GB of models. This may take 10-30 minutes depending on your internet connection.

### Memory Requirements

- Minimum: 8GB RAM
- Recommended: 16GB+ RAM
- Models will use ~2-4GB RAM during inference

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

Please refer to the original F5-TTS repository for license information.

## 🙏 Acknowledgments

- Original F5-TTS model by [hynt](https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice)
- Based on the F5-TTS architecture

## 📞 Support

If you encounter issues:
1. Check the Troubleshooting section above
2. Ensure all dependencies are installed correctly
3. Verify FFmpeg installation: `ffmpeg -version`
4. Check that you're using the correct conda environment

---

**Last Updated**: 2024
**Tested on**: macOS with Apple Silicon (M1/M2/M3)
