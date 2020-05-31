# -*- coding: utf-8 -*-
import time
import shutil
import datetime
import os
import json as js

def read_config():
    with open("config/mirror.json") as json_file:
        config = js.load(json_file)
    return config
conf=read_config()
system_type=conf['system']
mirror_folder=conf['folder']
language=conf['language']
server_type=conf['server']

help_msg='''
§r======= §6Minecraft Mirror 镜像服插件 §r=======
使用§6!!mirror sync§r来同步主服务器到镜像服
使用§6!!mirror start§r来打开镜像服
§4请注意：你只能在镜像服中关闭镜像服，要使用此功能，可以尝试使用
§4无需MCDR-Admin权限的§6SimpleOP
§4或者需要MCDR-Admin权限的§6StartStopHelper
'''
help_msg_en='''
§r======= §6Minecraft Mirror Plugin §r=======
Use §6!!mirror sync§r to sync the main server's world to the mirror one
Use §6!!mirror start§r to turn on the mirror server
§4CAUTIONS: YOU CAN ONLY TURN OFF THE MIRROR SERVER INSIDE
§4IF YOU WANT TO DO THAT, YOU CAN TRY THE PLUGIN
§6SimpleOP §rwithout MCDR-Admin permission required
§6StartStopHelper §r with MCDR-Admin permission required
'''
SimpleOP=' {"text":"§6查看SimpleOP","clickEvent":{"action":"open_url","value":"https://github.com/GamerNoTitle/SimpleOP"}}'
StartStopHelper=' {"text":"§6查看StartStopHelper","clickEvent":{"action":"open_url","value":"https://github.com/MCDReforged-Plugins/StartStopHelper"}}'
SimpleOP_en=' {"text":"§6Checkout SimpleOP","clickEvent":{"action":"open_url","value":"https://github.com/GamerNoTitle/SimpleOP"}}'
StartStopHelper_en=' {"text":"§6Checkout StartStopHelper","clickEvent":{"action":"open_url","value":"https://github.com/MCDReforged-Plugins/StartStopHelper"}}'
source='./server/world'
source_nether='./server/world_nether'
source_the_end='./server/world_the_end'
target=('{}server/world'.format(mirror_folder))
target_nether=('{}server/world_nether'.format(mirror_folder))
target_the_end=('{}server/world_the_end'.format(mirror_folder))

def on_info(server, info):
	if info.is_player and info.content == '!!mirror':
		if language=='zh-CN':
			server.tell(info.player, help_msg)
			server.execute('tellraw '+ info.player + SimpleOP)
			server.execute('tellraw '+ info.player + StartStopHelper)
		else:
			server.tell(info.player, help_msg_en)
			server.execute('tellraw '+ info.player + SimpleOP_en)
			server.execute('tellraw '+ info.player + StartStopHelper_en)

	if info.content == '!!mirror sync':
		start_time=datetime.datetime.now()
		server.execute('save-all')
		if language=='zh-CN':
			server.say('正在同步到镜像服……')
		else:
			server.say('Syncing...Please Wait...')
		if server_type!=0:
			try:
				shutil.copytree(source,target)
				shutil.copytree(source_nether,target_nether)
				shutil.copytree(source_the_end,target_the_end)
			except:
				shutil.rmtree(target,True)
				shutil.rmtree(target_nether,True)
				shutil.rmtree(target_the_end,True)
				shutil.copytree(source,target)
				shutil.copytree(source_nether,target_nether)
				shutil.copytree(source_the_end,target_the_end)
		else:
			try:
				shutil.copytree(source,target)
			except:
				shutil.rmtree(target,True)
				shutil.copytree(source,target)
		end_time=datetime.datetime.now()
		if language=='zh-CN':
			server.say('同步完成！用时{}'.format(end_time-start_time))
		else:
			server.say('Finished the opreation in {}'.format(end_time-start_time))

	if info.content == '!!mirror start':
		if language=='zh-CN':
			server.say('已执行镜像服开启操作！镜像服开启用时由服务器决定，一般为1~3分钟')
		else:
			server.say('Now starting the server, please wait...The time for the server\'s start depends on the server')
		if system_type==0:
			os.system('cd {} && python3 ./MCDReforged.py'.format(mirror_folder))
		if system_type==1:
			os.system('cd {} && python ./MCDReforged.py'.format(mirror_folder))
		os.system('cd ..')
		if language=='zh-CN':
			server.say('镜像服已关闭！')
		else:
			server.say('Mirror Server has been terminated!')