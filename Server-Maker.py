#import modules
import os
from subprocess import call

#Get Ver from User
print("What Server Would You Like To Install?\nA. Vanilla\nB. Forge\nC. Spigot")
version = input("Type A, B or C\n\n")

#Install Version
if version == "A":

    f4 = open("Vanilla.bat", "w+")
    f4.write("curl http://download1580.mediafire.com/n09jy7s72bzg/tdfmirbkydowm3h/Vanilla.py -O Vanilla.py")
    f4.close()

    call("Vanilla.bat")

    os.remove("Vanilla.bat")

    import Vanilla

elif version == "B":

    f3 = open("Forge.bat", "w+")
    f3.write("curl https://download1325.mediafire.com/8l5uag2ejqcg/bdph0rrb6zi01rl/Forge.py -O Forge.py")
    f3.close()

    call("Forge.bat")

    os.remove("Forge.bat")
    
    import Forge

elif version == "C":
    
    f2 = open("Spigot.bat", "w+")
    f2.write("curl http://download1594.mediafire.com/yqdusi2kkexg/g4zfspzjmtbmira/Spigot.py -O Spigot.py")
    f2.close()

    call("Spigot.bat")

    os.remove("Spigot.bat")

    import Spigot
    
