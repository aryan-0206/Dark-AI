# 🤖 Dark AI - Voice Assistant (Fixed Version)

## ✅ What Was Fixed

This is a **fully debugged and improved version** of Dark AI with all errors corrected and security improvements implemented.

### 🔧 Critical Fixes

1. **Alarm.py**
   - ❌ **Original Issue**: Alarm exit logic was incorrect - would check time BEFORE alarm rang
   - ✅ **Fixed**: Now properly waits 30 seconds AFTER alarm rings before exiting
   - ✅ Added error handling for missing files
   - ✅ Added input validation

2. **Calculatenumbers.py**
   - ❌ **Original Issue**: Typo "vlaue" instead of "value"
   - ❌ **Security**: Hardcoded API key in source code
   - ✅ **Fixed**: All typos corrected
   - ✅ **Security**: API key now loaded from environment variable
   - ✅ Added comprehensive error handling

3. **Dictapp.py**
   - ❌ **Original Issue**: Missing space in `os.system(f"start{dictapp[app]}")`
   - ❌ **Original Issue**: Missing space in `taskkill/ f/ im{dictapp[app]}`
   - ✅ **Fixed**: Proper string formatting with spaces
   - ✅ Added error handling for failed operations

4. **SearchNow.py**
   - ❌ **Original Issue**: Used `recognize_google_cloud` (requires paid API)
   - ❌ **Original Issue**: No input validation
   - ✅ **Fixed**: Changed to `recognize_google` (free)
   - ✅ Added `.strip()` to remove whitespace
   - ✅ Added proper exception handling for Wikipedia

5. **NewsRead.py**
   - ❌ **Security**: Exposed API key in source code
   - ❌ **Original Issue**: Poor input validation in continuation loop
   - ✅ **Security**: API key now from environment variable
   - ✅ **Fixed**: Better input handling and error messages
   - ✅ Added timeout for network requests

6. **Whatsapp.py**
   - ❌ **Security**: Hardcoded phone numbers (privacy issue)
   - ❌ **Original Issue**: No validation of phone numbers
   - ✅ **Fixed**: Phone numbers now in separate config file
   - ✅ Added JSON configuration system
   - ✅ Added validation for phone numbers

7. **intro.py**
   - ❌ **Original Issue**: No error handling for missing GIF file
   - ✅ **Fixed**: Added file existence check
   - ✅ Added proper exception handling

8. **Todo_List.py**
   - ❌ **Original Issue**: Function name typo `deletete_task` instead of `delete_task`
   - ❌ **Original Issue**: `view_task(task)` called with undefined variable
   - ✅ **Fixed**: Corrected function name
   - ✅ **Fixed**: `view_tasks()` now takes no arguments

9. **Dark_AI.py**
   - ❌ **Original Issue**: Weak password validation
   - ❌ **Original Issue**: No error handling in main loop
   - ❌ **Original Issue**: Potential infinite loops
   - ✅ **Fixed**: Comprehensive error handling throughout
   - ✅ **Fixed**: Better password validation
   - ✅ **Fixed**: Graceful error recovery
   - ✅ Added try-except blocks for all operations

### 🔒 Security Improvements

- ✅ API keys moved to environment variables
- ✅ Phone numbers in separate config file (not in code)
- ✅ Input validation on all user inputs
- ✅ Better password handling
- ✅ Sanitized error messages (don't expose system info)

### 🎯 Code Quality Improvements

- ✅ Consistent error handling across all modules
- ✅ Added docstrings to all functions
- ✅ Better code organization
- ✅ Removed code duplication
- ✅ Added input validation everywhere
- ✅ More informative error messages

---

## 📋 Installation & Setup

### Prerequisites

```bash
# Python 3.7 or higher required
python --version
```

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure API Keys

1. Copy the environment template:
```bash
copy .env.template .env
```

2. Edit `.env` and add your API keys:
```
WOLFRAM_API_KEY=your_actual_key_here
NEWS_API_KEY=your_actual_key_here
```

Get API keys from:
- WolframAlpha: https://products.wolframalpha.com/api/
- News API: https://newsapi.org/

### Step 3: Configure WhatsApp Contacts

Edit `whatsapp_config.json` with your contacts:
```json
{
    "1": {
        "name": "Mom",
        "phone": "+919876543210"
    },
    "2": {
        "name": "Friend",
        "phone": "+919123456789"
    }
}
```

### Step 4: Add Media Files

Place these files in the same directory:
- `zoro.gif` - Intro animation (optional)
- `music.mp3` - Alarm sound (optional)
- `notification.mp3` - Notification sound (optional)

### Step 5: Run Dark AI

```bash
python Dark_AI.py
```

**Default Password**: `Dark AI`

---

## 🎯 Usage

### Commands

#### General
- "wake up" - Activate assistant
- "hello" - Greeting
- "how are you" - Check status
- "thank you" - Thank assistant
- "go to sleep" - Deactivate (stay running)
- "finally sleep" - Exit program

#### Information
- "what time is it" - Get current time
- "weather" / "temperature" - Get weather info
- "news" - Get latest news (specify category)

#### Search
- "google [query]" - Search Google
- "youtube [query]" - Search YouTube
- "wikipedia [query]" - Search Wikipedia

#### Calculations
- "calculate 5 plus 5" - Perform calculations

#### Tasks & Schedule
- "schedule my day" - Add tasks
- "show my schedule" - View tasks

#### Memory
- "remember that [info]" - Store information
- "what do you remember" - Recall stored info

#### Controls
- "pause" / "play" - YouTube control
- "mute" - Mute video
- "volume up" / "volume down" - Adjust volume

#### Applications
- "open [app name]" - Open application
- "close [app name]" - Close application
- "close [number] tabs" - Close browser tabs

#### Communication
- "whatsapp" - Send WhatsApp message

#### Alarm
- "set an alarm" - Set alarm (format: HH and MM and SS)

#### System
- "internet speed" - Check connection speed
- "change password" - Update password
- "shut down the system" - Shutdown computer

#### Entertainment
- "tired" / "play music" - Play random music

---

## 📁 File Structure

```
dark_ai_fixed/
├── Dark_AI.py              # Main program
├── Alarm.py                # Alarm functionality
├── Calculatenumbers.py     # Calculator
├── Dictapp.py              # App control
├── GreetMe.py              # Greeting system
├── intro.py                # Intro animation
├── keyboard.py             # Volume control
├── NewsRead.py             # News reader
├── SearchNow.py            # Search functions
├── Todo_List.py            # Todo list manager
├── Whatsapp.py             # WhatsApp integration
├── Alarmtext.txt           # Alarm storage
├── password.txt            # Password storage
├── Remember.txt            # Memory storage
├── tasks.txt               # Task storage
├── whatsapp_config.json    # WhatsApp contacts
├── .env.template           # API key template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🐛 Error Messages Explained

### "ModuleNotFoundError"
**Solution**: Install missing packages
```bash
pip install [package-name]
```

### "API key not configured"
**Solution**: Set up `.env` file with your API keys

### "Could not understand audio"
**Solution**: 
- Check microphone is connected
- Speak clearly
- Reduce background noise

### "Password file not found"
**Solution**: File will be created automatically with default password "Dark AI"

### "Application not found"
**Solution**: Check spelling or add app to `dictapp` dictionary in `Dictapp.py`

---

## 🔒 Security Best Practices

1. **Never commit `.env` to version control**
   - Add `.env` to `.gitignore`

2. **Keep API keys secret**
   - Don't share your `.env` file
   - Regenerate keys if exposed

3. **Update `whatsapp_config.json`**
   - Remove default placeholder numbers
   - Don't commit real phone numbers

4. **Change default password**
   - Use "change password" command
   - Or edit `password.txt`

---

## 🧪 Testing

### Test Individual Modules

```bash
# Test calculator
python Calculatenumbers.py

# Test todo list
python Todo_List.py

# Test search
python SearchNow.py
```

### Test Main Program

```bash
python Dark_AI.py
```

1. Enter password: `Dark AI`
2. Say: "wake up"
3. Try commands from the usage section

---

## 🔧 Troubleshooting

### No audio output
1. Check speakers/headphones
2. Check volume level
3. Reinstall pyttsx3: `pip install pyttsx3 --upgrade`

### Voice recognition not working
1. Check microphone permissions
2. Test microphone in other apps
3. Adjust `r.energy_threshold` in `takeCommand()` function

### Import errors
1. Install all dependencies: `pip install -r requirements.txt`
2. Ensure all files are in the same directory
3. Check Python version (3.7+)

### WhatsApp not sending
1. Check `whatsapp_config.json` has valid phone numbers
2. Ensure WhatsApp Web is logged in
3. Check internet connection

---

## 📊 Comparison: Before vs After

| Issue | Before | After |
|-------|--------|-------|
| Alarm Logic | ❌ Never exits | ✅ Exits after 30s |
| API Keys | ❌ Hardcoded | ✅ Environment vars |
| Error Handling | ❌ None | ✅ Comprehensive |
| Input Validation | ❌ Minimal | ✅ Thorough |
| Code Quality | ❌ Typos, bugs | ✅ Clean, tested |
| Security | ❌ Exposed data | ✅ Secure |
| User Experience | ❌ Crashes often | ✅ Robust |

---

## 📝 Changelog

### Version 2.0 (Fixed)

**Bug Fixes:**
- Fixed Alarm.py exit logic
- Fixed typos in all modules
- Fixed string formatting errors
- Fixed function name errors
- Fixed undefined variable references
- Fixed speech recognition API calls

**Security:**
- Moved API keys to environment variables
- Externalized WhatsApp contacts to JSON
- Improved password validation
- Sanitized error messages

**Improvements:**
- Added comprehensive error handling
- Added input validation everywhere
- Added better user feedback
- Added configuration templates
- Improved code organization
- Added docstrings to all functions

**New Files:**
- `.env.template` - API key configuration
- `whatsapp_config.json` - Contact management
- `README.md` - Complete documentation
- `requirements.txt` - Dependency list

---

## 🚀 Future Enhancements

Possible improvements for future versions:
- [ ] Web interface
- [ ] Mobile app
- [ ] Cloud synchronization
- [ ] Multi-language support
- [ ] Machine learning integration
- [ ] Custom wake word
- [ ] Voice profiles (multiple users)
- [ ] Database integration
- [ ] API server mode

---

## 📄 License

This is a fixed version of Dark AI for educational purposes.

---

## 🙏 Acknowledgments

Original concept by Dark AI developer
Fixed and improved version with:
- Bug fixes
- Security enhancements
- Code quality improvements
- Comprehensive documentation

---

## 📞 Support

If you encounter any issues:
1. Check this README
2. Review error messages carefully
3. Ensure all dependencies are installed
4. Verify configuration files are correct
5. Test individual modules

---

**Dark AI Fixed - Version 2.0**
*Ready for production use!*
#   D a r k - A I  
 