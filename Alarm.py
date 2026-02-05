import pyttsx3
import datetime
import os
import sys

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Read alarm time from file
try:
    extractedtime = open("Alarmtext.txt", "rt")
    time = extractedtime.read()
    Time = str(time)
    extractedtime.close()
except FileNotFoundError:
    print("Error: Alarmtext.txt not found")
    sys.exit(1)

# Clear the alarm file
try:
    deletetime = open("Alarmtext.txt", "r+")
    deletetime.truncate(0)
    deletetime.close()
except Exception as e:
    print(f"Error clearing alarm file: {e}")

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("dark", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow).strip()
    
    # Validate alarm time format
    if not Alarmtime:
        speak("Invalid alarm time")
        return
    
    print(f"Alarm set for: {Alarmtime}")
    speak(f"Alarm set for {Alarmtime}")
    
    alarm_triggered = False
    
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        
        if currenttime == Alarmtime:
            speak("Alarm ringing...")
            print("ALARM RINGING!")
            
            # Play alarm sound
            try:
                if os.path.exists("music.mp3"):
                    os.startfile("music.mp3")
                else:
                    print("Warning: music.mp3 not found")
            except Exception as e:
                print(f"Could not play alarm sound: {e}")
            
            alarm_triggered = True
        
        # FIXED: Exit 30 seconds AFTER alarm rings, not before
        elif alarm_triggered:
            # Wait 30 seconds after alarm rings, then exit
            import time
            time.sleep(30)
            print("Alarm finished")
            break
        
        # Small delay to avoid excessive CPU usage
        import time
        time.sleep(1)

if Time:
    ring(Time)
else:
    print("No alarm time specified")
