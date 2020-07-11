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
§r======= §6Minecraft Mirror 镜像服插件 §r=======
使用§6!!mirror sync§r来同步主服务器到镜像服
使用§6!!mirror start§r来打开镜像服
使用§6!!mirror abort§r来中断冷回档
§4请注意：如果你不开启镜像服的Rcon功能，你只能在镜像服中关闭镜像服
§4要使用此功能，可以尝试使用
§4无需MCDR-Admin权限的§6SimpleOP
§4或者需要MCDR-Admin权限的§6StartStopHelper
-----Rcon功能-----
使用§6!!mirror info§r来查看rcon配置信息（管理员）
使用§6!!mirror stop§r来关闭镜像服
使用§6!!mirror status§r来查看镜像服务器是否开启
使用§6!!mirror rcon <command>§r来在镜像服中执行命令（管理员，无需输入/）
'''

SimpleOP=' {"text":"§6查看SimpleOP","clickEvent":{"action":"open_url","value":"https://github.com/GamerNoTitle/SimpleOP"}}'
StartStopHelper=' {"text":"§6查看StartStopHelper","clickEvent":{"action":"open_url","value":"https://github.com/MCDReforged-Plugins/StartStopHelper"}}'

def helpmsg(server,info):
    if info.is_player and info.content == '!!mirror':
        server.tell(info.player, help_msg)
        server.execute('tellraw '+ info.player + SimpleOP)
        server.execute('tellraw '+ info.player + StartStopHelper)

def sync(server,info):
    start_time=datetime.datetime.now()
    server.execute('save-all')
    server.say('§6[Mirror]正在同步到镜像服……')
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
    # if(abort_sync):
    #     None
    # else:
    server.say('§6[Mirror]同步完成！用时{}'.format(end_time-start_time))

def start(server,info):
    server.say('§6[Mirror]已执行镜像服开启操作！镜像服开启用时由服务器决定，一般为1~3分钟')
    if platform.system()=='Windows':
        os.system('cd {} && powershell {}'.format(mirror_folder,start_command))
    else:
        os.system('cd {} && {}'.format(mirror_folder,start_command))
    os.system('cd ..')
    global mirror_started
    mirror_started=False
    server.say('§6[Mirror]镜像服已关闭！')

def command(server,info):
    if(conf['remote']['command']):
        if(server.get_permission_level(info)>2):
            try:
                with MCRcon(address,secret,port) as remote:
                    remote.command('/'+info.content[14:])
                    remote.disconnect()
            except Exception as e:
                server.tell(info.player,'§6[Mirror]§4连接错误：{}'.format(e))
        else:
            server.tell(info.player,'§6[Mirror]§4错误：权限不足')
    else:
        server.tell(info.player,' §6[Mirror]§4错误：rcon功能未开启！')

def stop(server,info):
    try:
        with MCRcon(address,secret,port) as remote:
            remote.command('/stop')
            remote.disconnect()
    except Exception as e:
        server.tell(info.player,'§6[Mirror]§4连接错误：{}'.format(e))


def information(server,info):
    if(server.get_permission_level(info)>2):
        server.tell(info.player,remote_info)
    else:
        server.tell(info.player,"§6[Mirror]§4错误：权限不足")

def status(server,info):
    global mirror_started
    try:
        with MCRcon(address,secret,port) as remote:
            remote.command('/list')
            remote.disconnect()
        server.tell(info.player,'§6[Mirror]§l镜像服已开启！')
    except Exception:
        if mirror_started:
            server.tell(info.player,'§6[Mirror]§l镜像服正在启动中……')
        else:
            server.tell(info.player,'§4[Mirror]§l镜像服未开启！')


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
