from mcstatus import MinecraftBedrockServer,MinecraftServer
from os import system, name
from time import sleep
from sys import argv,exit
from sty import fg

system("")
def clear():
    system('cls' if name=='nt' else 'clear')

def make_green(text):
    return f"{fg(10)}{text}{fg.rs}"

s = 'Usage: {} <ip> <pe or pc> (port)'.format(argv[0])
if len(argv) < 3 :
    exit(s)
print("minecraft ping checker | by larina\n")
ip = argv[1]
port = None
a=1
try :
    port = argv[3]
except:
    pass
if argv[2] == "pe":
    port = port or 19132
    type="UDP"
    a = 1000
    server = MinecraftBedrockServer.lookup(f"{ip}:{port}")
elif argv[2] == "pc":
    port = port or 25565
    type="TCP"
    server = MinecraftServer.lookup(f"{ip}:{port}")
else:
    exit(s)

while True :
    #clear()
    try :
        try:
            status = server.status()
            try :
                players_online = status.players_online
                players_max = status.players_max
            except:
                players_online = status.players.online
                players_max = status.players.max
            print(f"Connected to {make_green(ip)}: time={make_green(str(int(status.latency * a))+ 'ms')} players={make_green(players_online)}/{make_green(players_max)} protocol={make_green(type)} port={make_green(port)}")
            #print(f"ip : {ip} | ping : {status.latency} | players : {status.players_online}/{status.players_max} | motd : {status.motd}")
        except:
            print(f"{fg(9)}Connection timed out{fg.rs}")
        sleep(2)
    except:
        print("\nBye")
        break
