# -*- coding: utf-8 -*-
import time
import shutil
import datetime
import os
import json as js
import platform
def read_config():
    with open("config/mirror.json") as json_file:
        config = js.load(json_file)
    return config
conf=read_config()

mirror_folder=conf['path']
remote_enable=conf['remote']['enable']
address=conf['remote']['address']
port=conf['remote']['port']
secret=conf['remote']['secret']
start_command=conf['command']
world=conf["world"]
source=[]
target=[]
delay=conf['delay']
abort_sync=False
mirror_started=False

MCDRJudge=os.path.exists("{}MCDReforged.py".format(mirror_folder))

for i in range(len(world)):
    source.append('./server/{}'.format(world[i-1]))

if(MCDRJudge):
    for i in range(len(world)):
        target.append('{}/server/{}'.format(mirror_folder,world[i-1]))
else:
    for i in range(len(world)):
        target.append('{}/{}'.format(mirror_folder,world[i-1]))

if(remote_enable):
    from mcrcon import MCRcon


remote_info='''
§6[Mirror]§bRemote Information:
§5Rcon Address: §b{}
§5Rcon Port: §b{}
'''.format(address,port)

help_msg='''
§r======= §6Minecraft Mirror Plugin §r=======
Use §6!!mirror sync§r to sync the main server's world to the mirror one
Use §6!!mirror start§r to turn on the mirror server
Use §6!!mirror abort§r to stop the cold sync process
§4BE CAUTIOUS: IF YOU DON'T ENABLE THE RCON FREATURE OF THE MIRROR SERVER, YOU CANNOT SHUTDOWN THE SERVER BY REMOTE COMMAND
§4YOU CAN ONLY SHUTDOWN IT IN THE MIRROR SERVER, TO DO THIS, YOU CAN CHECKOUT THE FOLLOWING MCDR PLUGINS
§4SimpleOP without MCDR-Admin permission required
§4StartStopHelper with MCDR-Admin permission required
-----Rcon Features-----
Use §6!!mirror info§r to checkout rcon information(MCDR-Admin Permission is Required)
Use §6!!mirror stop§r to stop mirror server
Use §6!!mirror status§r to checkout whether the mirror has been turned on or not
Use §6!!mirror rcon <command>§r to send command to mirror server(MCDR-Admin Permission is Required, use it WITHOUT SLASH)
'''

SimpleOP=' {"text":"§6Checkout SimpleOP","clickEvent":{"action":"open_url","value":"https://github.com/GamerNoTitle/SimpleOP"}}'
StartStopHelper=' {"text":"§6Checkout StartStopHelper","clickEvent":{"action":"open_url","value":"https://github.com/MCDReforged-Plugins/StartStopHelper"}}'


def helpmsg(server,info):
    if info.is_player and info.content == '!!mirror':
        server.tell(info.player, help_msg)
        server.execute('tellraw '+ info.player + SimpleOP)
        server.execute('tellraw '+ info.player + StartStopHelper)

def sync(server,info):
    start_time=datetime.datetime.now()
    server.execute('save-all')
    server.say('§6[Mirror]Syncing...')
    i=0
    try:
        while True:
            if(i>len(world)-1): break
            shutil.copytree(source[i],target[i])
            i=i+1
    except:
        try:
            while True:
                if(i>len(world)-1): break
                shutil.rmtree(target[i],True)
                shutil.copytree(source[i],target[i])
                i=i+1
        except Exception as e:
            server.say('§4[Mirror]Hot Sync Failed：{}'.format(e))
            server.say('§6[Mirror]§rServer will be turned off for the puepose to sync in {} Seconds'.format(delay))
            count=delay
            global abort_sync
            while True:
                time.sleep(1)
                aborted=abort_sync
                if(aborted):
                    break
                count=count-1
                server.say('§6[Mirror]{} second(s) left'.format(count))
                if(count==0):
                    break
            time.sleep(delay)
            if(abort_sync==False):
                server.execute('kick @a §6[Mirror]Syncing the world...')
                server.stop()
                server.wait_for_start()
                while True:
                    if(i>len(world)-1): break
                    shutil.rmtree(target[i],True)
                    shutil.copytree(source[i],target[i])
                    i=i+1
                server.start()
    end_time=datetime.datetime.now()
    if(abort_sync):
        None
    else:
        server.say('§6[Mirror]Sync completed in {}'.format(end_time-start_time))
    abort_sync=False

def start(server,info):
    server.say('§6[Mirror]Mirror server is launching, please wait...')
    if platform.system()=='Windows':
        os.system('cd {} && powershell {}'.format(mirror_folder,start_command))
    else:
        os.system('cd {} && {}'.format(mirror_folder,start_command))
    os.system('cd ..')
    global mirror_started
    mirror_started=False
    server.say('§6[Mirror]Mirror server has been shutdown!')

def command(server,info):
    if(conf['remote']['command']):
        if(server.get_permission_level(info)>2):
            try:
                with MCRcon(address,secret,port) as remote:
                    remote.command('/'+info.content[14:])
                    remote.disconnect()
            except Exception as e:
                server.tell(info.player,'§6[Mirror]§4Connection Failed: {}'.format(e))
        else:
            server.tell(info.player,'§6[Mirror]§4Error: Permission Denied!')
    else:
        server.tell(info.player,' §6[Mirror]§4Error: Rcon feature is disabled!')

def stop(server,info):
    try:
        with MCRcon(address,secret,port) as remote:
            remote.command('/stop')
            remote.disconnect()
    except Exception as e:
        server.tell(info.player,'§6[Mirror]§4Connection Failed: {}'.format(e))


def information(server,info):
    if(server.get_permission_level(info)>2):
        server.tell(info.player,remote_info)
    else:
        server.tell(info.player,"§6[Mirror]§4Error: Permission Denied!")

def status(server,info):
    try:
        with MCRcon(address,secret,port) as remote:
            remote.command('/list')
            remote.disconnect()
        server.tell(info.player,'§6[Mirror]§lMirror Server is online!')
    except Exception:
        if mirror_started:
            server.tell(info.player,'§6[Mirror]§lMirror Server is Starting...')
        else:
            server.tell(info.player,'§4[Mirror]§lMirror Server is offline!')


def on_info(server,info):
    if info.is_player and info.content == '!!mirror':
        helpmsg(server,info)

    if info.content == '!!mirror sync':
        sync(server,info)
    
    if info.content == '!!mirror start':
        global mirror_started
        mirror_started=True
        start(server,info)

    if('!!mirror rcon' in info.content):
        command(server,info)
    
    if(info.content=='!!mirror info'):
        information(server,info)

    if(info.content=='!!mirror stop'):
        stop(server,info)

    if(info.content=='!!mirror status'):
        status(server,info)
    
    if(info.content=='!!mirror abort'):
        global abort_sync
        abort_sync=True
        server.say('§6[Mirror]§lCold sync has been aborted by§r§b{}'.format(info.player))