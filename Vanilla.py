#import modules
import os
import time
import subprocess
import fnmatch
import shutil
import stat
from subprocess import call
from datetime import datetime

#Install and import requests module

f5 = open("req.bat", "w+")
f5.write("python3 -m pip install requests")
f5.close()

call("req.bat")

import requests


#Create and run bat file to download server file
print("Downloading latest server...")

time.sleep(3)

url = 'https://www.minecraft.net/en-us/download/server/'
a = requests.get(url)
b = a.text

start = b.find("https://launcher.mojang.com/")
end = b.find("server.jar")
sub = b[start:end]

f4 = open("dl.bat", "w+")
f4.write("curl " + sub + "server.jar -O server.jar")
f4.close()

call("dl.bat")


#Create and write txt file to agree to the EULA to reduce required user input
print("Server downloaded, Creating EULA...")

f2 = open("eula.txt", "w+")
f2.write("eula=True")
f2.close()



word=datetime.today().strftime("%A")
pre1 = word[0:3]

now = datetime.now()

current_time = now.strftime(" %b %d %H:%M:%S %z")

year = now.strftime(" %Y")

import datetime
tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
pre2 = tz[0:3]


f1 = open("server.txt", "w+")
f1.write("#Minecraft server properties\n#" + pre1 + current_time + pre2 + year + "\nspawn-protection=0\nmax-tick-time=60000\nquery.port=25565\ngenerator-settings=\nsync-chunk-writes=true\nforce-gamemode=false\nallow-nether=true\nenforce-whitelist=false\ngamemode=survival\nbroadcast-console-to-ops=true\nenable-query=false\nplayer-idle-timeout=0\ntext-filtering-config=\ndifficulty=easy\nspawn-monsters=true\nbroadcast-rcon-to-ops=true\nop-permission-level=4\npvp=true\nentity-broadcast-range-percentage=100\nsnooper-enabled=true\nlevel-type=default\nhardcore=false\nenable-status=true\nenable-command-block=false\nmax-players=20\nnetwork-compression-threshold=256\nresource-pack-sha1=\nmax-world-size=29999984\nfunction-permission-level=2\nrcon.port=25575\nserver-port=34625\ndebug=false\nserver-ip=\nspawn-npcs=true\nallow-flight=false\nlevel-name=world\nview-distance=10\nresource-pack=\nspawn-animals=true\nwhite-list=false\nrcon.password=\ngenerate-structures=true\nmax-build-height=256\nonline-mode=true\nlevel-seed=\nuse-native-transport=true\nprevent-proxy-connections=false\nenable-jmx-monitoring=false\nenable-rcon=false\nrate-limit=0\nmotd=\\u00A76Lmao")
f1.close()

os.rename("server.txt", "server.properties")

#Create start.bat file for user to run the server and server.properties
print("EULA created, Making server start script and properties...")
ram = input("how much RAM would you like? (in GB)\n")

time.sleep(3)

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "minecraft_server.*.*.*.jar"):
        os.rename(file, "server.jar")

f0 = open("start.bat", "w+")
f0.write(":begin\n\njava -Xmx" + ram + "G -Xms" + ram + "G -jar server.jar nogui\n\ntimeout 3\n\necho resuming server...\n\ngoto:begin")
f0.close()

#Remove files and folders related to this script e.g. dl.bat
print("Complete! Cleaning folder...")

time.sleep(3)

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*.*.*.json"):
        os.remove(file)

os.remove("dl.bat")
os.remove("req.bat")

#Run the server
print("Done! Starting Server!")

time.sleep(3)

subprocess.call("start.bat")
