# 🚀 Dark AI - Quick Start Guide

## Installation (5 Minutes)

### Step 1: Extract Files
Extract the "Dark AI.zip" to a folder on your computer.

### Step 2: Install Python Packages
Open terminal/command prompt in the extracted folder and run:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies.

### Step 3: Configure API Keys (Optional but Recommended)

1. Copy `.env.template` to `.env`:
   ```bash
   copy .env.template .env
   ```

2. Edit `.env` and add your API keys:
   ```
   WOLFRAM_API_KEY=your_key_here
   NEWS_API_KEY=your_key_here
   ```

Get free API keys from:
- WolframAlpha: https://products.wolframalpha.com/api/
- News API: https://newsapi.org/

**Note**: Program will work without these, but some features will be limited.

### Step 4: Configure WhatsApp (Optional)

Edit `whatsapp_config.json` with your contacts:
```json
{
    "1": {
        "name": "Friend Name",
        "phone": "+919876543210"
    }
}
```

### Step 5: Run Dark AI

```bash
python Dark_AI.py
```

**Default Password**: `Dark AI`

---

## First Run

1. **Enter Password**: Type `Dark AI` and press Enter
2. **Wake Up Dark AI**: Say "wake up" (or type it if mic not working)
3. **Try Commands**: See examples below

---

## Quick Test Commands

Try these to test if everything works:

```
✅ "hello" - Greeting
✅ "what time is it" - Get time
✅ "calculate 5 plus 5" - Math
✅ "open notepad" - Open app
✅ "google search python" - Web search
```

---

## Common Issues & Solutions

### "No module named 'pyttsx3'"
**Solution**: 
```bash
pip install -r requirements.txt
```

### Voice recognition not working
**Solutions**:
- Check microphone is plugged in
- Grant microphone permissions
- Speak clearly and loud enough
- Alternatively, type commands instead

### "API key not configured"
**Solution**: This is just a warning. Program still works, but:
- News feature needs NEWS_API_KEY
- Calculator needs WOLFRAM_API_KEY

---

## File Overview

```
Dark AI/
├── Dark_AI.py           ⭐ Main program - RUN THIS
├── requirements.txt     📦 Install these first
├── README.md           📖 Full documentation
├── ERROR_REPORT.md     🐛 What was fixed
├── QUICK_START.md      🚀 This file
├── .env.template       🔑 API key template
├── whatsapp_config.json 📱 WhatsApp contacts
└── (other .py files)   🔧 Support modules
```

---

## Need Help?

1. **Full Documentation**: Read `README.md`
2. **Error Details**: Check `ERROR_REPORT.md`
3. **Can't Run**: Ensure Python 3.7+ is installed

---

## What's New in This Fixed Version?

✅ Fixed 23 bugs in original code
✅ Added comprehensive error handling
✅ Improved security (API keys, phone numbers)
✅ Better user experience
✅ Complete documentation
✅ Production-ready code

---

## Pro Tips

1. **Change Password**: Say "change password" after waking up
2. **Keyboard Shortcuts**: Ctrl+C to exit anytime
3. **Config Files**: Edit .env and whatsapp_config.json for personalization
4. **Test First**: Try basic commands before complex ones

---

**Ready to go!** 🎉

Say "wake up" and start using Dark AI!
