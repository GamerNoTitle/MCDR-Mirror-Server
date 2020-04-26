# -*- coding: utf-8 -*-
import time
import shutil
import datetime
import os
system_type=0	# 0为linux，1为windows
mirror_folder='./mirror/'	# 在这里设置镜像服的文件夹，默认为./mirror/
help_msg='''
§r======= §6Minecraft Mirror 镜像服插件 §r=======
使用§6!!mirror sync§r来同步主服务器到镜像服
使用§6!!mirror start§r来打开镜像服
§4请注意：你只能在镜像服中关闭镜像服，要使用此功能，可以尝试使用
§4无需MCDR-Admin权限的§6SimpleOP
§4或者需要MCDR-Admin权限的§6StartStopHelper
'''
SimpleOP=' {"text":"§6查看SimpleOP","clickEvent":{"action":"open_url","value":"https://github.com/GamerNoTitle/SimpleOP"}}'
StartStopHelper=' {"text":"§6查看StartStopHelper","clickEvent":{"action":"open_url","value":"https://github.com/MCDReforged-Plugins/StartStopHelper"}}'
source='./server/world'
target=('{}server/world'.format(mirror_folder))
def on_info(server, info):
	if info.is_player and info.content == '!!mirror':
		server.tell(info.player, help_msg)
		server.execute('tellraw '+ info.player + SimpleOP)
		server.execute('tellraw '+ info.player + StartStopHelper)

	if info.content == '!!mirror sync':
		start_time=datetime.datetime.now()
		server.execute('save-all')
		server.say('正在同步到镜像服……')
		try:
			shutil.copytree(source,target)
		except:
			shutil.rmtree(target,True)
			shutil.copytree(source,target)
		end_time=datetime.datetime.now()
		server.say('同步完成！用时{}'.format(end_time-start_time))

	if info.content == '!!mirror start':
		server.say('已执行镜像服开启操作！镜像服开启用时由服务器决定，一般为1~3分钟')
		if system_type==0:
			os.system('cd mirror && python3 ./MCDReforged.py')
		if system_type==1:
			os.system('cd mirror && python ./MCDReforged.py')
		os.system('cd ..')
		server.say('镜像服已关闭！')