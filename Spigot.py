#import modules
import os
import time
import fnmatch
import shutil
import stat
from subprocess import call
from datetime import datetime


#Create and run bat file to download buildtools.jar
print("Downloading buildtools...")

time.sleep(3)

f4 = open("dl.bat","w+")
f4.write("curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar")
f4.close()

call("dl.bat")

#Create and run bat file to build latest spigot using buildtools.jar
print("Building spigot server file...")

time.sleep(3)

f3 = open("build.bat", "w+")
f3.write("java -jar buildtools.jar --rev latest")
f3.close()

call("build.bat")

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*-*.*.*.jar"):
        os.rename(file, "server.jar")

#Create and write txt file to agree to the EULA to reduce required user input
print("Spigot file built, Creating EULA and server.properties...")


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

f1 = open("start.bat", "w+")
f1.write(":begin\n\njava -DIReallyKnowWhatIAmDoingISwear -Xmx" + ram + "G -Xms" + ram + "G -jar server.jar nogui -o true\n\ntimeout 3\n\necho resuming server...\n\ngoto:begin")
f1.close()

#Remove files and folders related to buildtools and this script e.g. dl.bat
print("Complete! Cleaning folder...")

time.sleep(3)

# Apache
os.chmod("apache-maven-3.6.0", stat.S_IWRITE)
shutil.rmtree("apache-maven-3.6.0")
#
#
#
#
#
# BuildData
dir = r'BuildData'

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)
os.chmod("BuildData", stat.S_IWRITE)
shutil.rmtree("BuildData")
#
#
#
#
#
# Bukkit
dir = r'Bukkit'

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)
os.chmod("Bukkit", stat.S_IWRITE)
shutil.rmtree("Bukkit")
#
#
#
#
#
# CraftBukkit
dir = r'CraftBukkit'

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)
os.chmod("CraftBukkit", stat.S_IWRITE)
shutil.rmtree("CraftBukkit")
#
#
#
#
#
# PortableGit
os.chmod("PortableGit-2.30.0-64-bit", stat.S_IWRITE)
shutil.rmtree("PortableGit-2.30.0-64-bit")
#
#
#
#
#
# Spigot
dir = r'Spigot'

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)
dir = r'Spigot\Spigot-API'

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)
dir = r'Spigot\Spigot-Server'

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)
os.chmod("Spigot", stat.S_IWRITE)
shutil.rmtree("Spigot")
#
#
#
#
#
# work  
os.chmod("work", stat.S_IWRITE)
shutil.rmtree("work")
#
#
#
#
#
# Other Files
os.remove("build.bat")
os.remove("dl.bat")
os.remove("BuildTools.jar")
os.remove("BuildTools.log.txt")

#Run the server
print("Done! Starting Server!")

time.sleep(3)

call("start.bat")
