#import modules
import os
import time
import fnmatch
import requests
from subprocess import call
from datetime import datetime


#Create and run bat file to download forge installer
print("Downloading forge installer...")

time.sleep(3)

url = 'https://files.minecraftforge.net/'
a = requests.get(url)
b = a.text

start = b.find("https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.")
end = b.find("-installer.jar")
sub = b[start:end]

f4 = open("dl.bat", "w+")
f4.write("curl " + sub + "-installer.jar -O Forge-Installer.jar")
f4.close())

call("dl.bat")

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*-*.*.*-*.*.*.jar"):
        os.rename(file, "forge-inst.jar")

#Create and run bat file to run forge installer
print("Running forge installer...")

time.sleep(3)

f3 = open("inst.bat", "w+")
f3.write("java -jar forge-inst.jar --installServer")
f3.close()

call("inst.bat")

#Create and write txt file to agree to the EULA to reduce required user input
print("Forge server downloaded, Creating EULA and server.properties...")



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

f2 = open("eula.txt", "w+")
f2.write("eula=True")
f2.close()

#Create start.bat file for user to run the server
print("EULA created, Making server start script...")
ram = input("how much RAM would you like? (in GB)\n")

time.sleep(3)

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*-*.*.*-*.*.*.jar"):
        os.rename(file, "forge.jar")

f1 = open("start.bat", "w+")
f1.write(":begin\n\njava -Xmx" + ram + "G -Xms" + ram + "G -jar forge.jar nogui\n\ntimeout 3\n\necho resuming server...\n\ngoto:begin")
f1.close()

#Remove files and folders related to this script e.g. dl.bat
print("Complete! Cleaning folder...")

time.sleep(3)

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*.*.*.json"):
        os.remove(file)

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "minecraft_server.*.*.*.jar"):
        os.remove(file)

os.remove("dl.bat")
os.remove("inst.bat")
os.remove("installer.log")
os.remove("forge-inst.jar")

#Run the server
print("Done! Starting Server!")

time.sleep(3)

call("start.bat")
