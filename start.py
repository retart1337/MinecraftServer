import os
config = """[PROPERTIES]
generator-settings=
op-permission-level=4
allow-nether=true
level-name=world
enable-query=false
allow-flight=false
announce-player-achievements=true
server-port=25565
max-world-size=29999984
level-type=flat
enable-rcon=false
level-seed=
force-gamemode=false
server-ip=127.0.0.1
network-compression-threshold=256
max-build-height=256
spawn-npcs=true
white-list=false
spawn-animals=true
hardcore=false
snooper-enabled=true
resource-pack-sha1=
online-mode=false
resource-pack=
pvp=true
difficulty=1
enable-command-block=false
gamemode=1
player-idle-timeout=0
max-players=20
max-tick-time=60000
spawn-monsters=true
generate-structures=true
view-distance=10
motd=PythonMine"""
if "server.properties" not in os.listdir():
    with open("server.properties", 'w') as cfg:
        cfg.write(config)
import server
def startfunc(factory):
    pass