# -*- coding: utf-8 -*-
import shutil
import datetime
import os
import json as js
import platform
from os.path import abspath, dirname
from utils import rcon
current_path = abspath(dirname(__file__))
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
    connection=rcon.Rcon(address,port,secret)


remote_info='''
§6[Mirror]§bRemote Information:
§5Rcon Address: §b{}
§5Rcon Port: §b{}
'''.format(address,port)

help_msg='''
§r======= §6Minecraft Mirror Plugin §r=======
Use §6!!mirror sync§r to sync the main server's world to the mirror one
Use §6!!mirror start§r to turn on the mirror server
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
        server.reply(info, help_msg, encoding=None)
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
        except Exception:
            while True:
                if(i>len(world)-1): break
                shutil.rmtree(target[i],True)
                ignore=shutil.ignore_patterns('session.lock')
                shutil.copytree(source[i],target[i],ignore=ignore)
                i=i+1

    end_time=datetime.datetime.now()
    server.say('§6[Mirror]Sync completed in {}'.format(end_time-start_time))

def start(server,info):
    server.say('§6[Mirror]Mirror server is launching, please wait...')
    if platform.system()=='Windows':
        os.system('cd {} && powershell {}'.format(mirror_folder,start_command))
    else:
        os.system('cd {} && {}'.format(mirror_folder,start_command))
    os.system('cd {}'.format(current_path))
    global mirror_started
    mirror_started=False
    server.say('§6[Mirror]Mirror server has been shutdown!')

def command(server,info):
    if(conf['remote']['command']):
        if(server.get_permission_level(info)>2):
            try:
                connection.connect()
                connection.send_command(info.content[14:])
                connection.disconnect()
                server.reply(info,'§6[Mirror]Command Sent!', encoding=None)
            except Exception as e:
                server.reply(info,'§6[Mirror]§4Error: {}'.format(e), encoding=None)
        else:
            server.reply(info,'§6[Mirror]§4Error: Permission Denied!', encoding=None)
    else:
        server.reply(info,' §6[Mirror]§4Error: Rcon feature is disabled!', encoding=None)

def stop(server,info):
    try:
        connection.connect()
        connection.send_command('stop')
        connection.disconnect()
    except Exception as e:
        server.reply(info,'§6[Mirror]§4Connection Failed: {}'.format(e), encoding=None)


def information(server,info):
    if(server.get_permission_level(info)>2):
        server.reply(info,remote_info)
    else:
        server.reply(info,"§6[Mirror]§4Error: Permission Denied!", encoding=None)

def status(server,info):
    global mirror_started
    try:
        connection.connect()
        server.reply(info,'§6[Mirror]§lMirror Server is online!', encoding=None)
        connection.disconnect()
    except:
        if mirror_started:
            server.reply(info,'§6[Mirror]§lMirror Server is Starting...(or mirror has been started but rcon feature didn\'t work well', encoding=None)
        else:
            server.reply(info,'§4[Mirror]§lMirror Server is offline!', encoding=None)

def on_load(server, old_module):
    server.add_help_message('!!mirror', '§6Get the usage of Mirror', encoding=None)

def on_info(server,info):
    if info.is_player and info.content == '!!mirror':
        helpmsg(server,info)

    if info.content == '!!mirror sync':
        sync(server,info)
    
    if info.content == '!!mirror start':
        global mirror_started
        if mirror_started:
            server.reply(info,'§b[Mirror]Mirror server has already started, please don\'t run the command again!', encoding=None)
        else:
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
    