import webbrowser
import time
#!/usr/bin/python

VAR = 0

print("This program started on "+time.ctime())
while (VAR < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=LRP8d7hhpoQ")
    VAR = VAR + 1
    
