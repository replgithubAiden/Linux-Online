import time
import sys

def write(str, eol = "\n"):
    for char in str:
        time.sleep(.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()

write("How too use this awesome kali tool")
write("First, cd into the kali directory like this, cd kali-online")
write("Second, run the file in terminal like this, sudo ./kali.sh or like this bash kali.sh")
write("Third, add an password for guacamole root user, than open your browser to go to your ip and the port that the terminal told you.")
write("thats it for the tutorial, see ya later ;)")
