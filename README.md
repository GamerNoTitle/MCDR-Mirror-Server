# MCDR-Mirror-Server

[ENGLISH](#English)

这是一个能够让你在MCDR的帮助下开镜像服便于调试的插件（仅支持python3）

> ### 2020/7/6
>
> 已知1.16以上版本会出现Session.lock文件被锁定的问题，目前采取了一种折中的方案，采用关服同步型的冷同步
>
> 后期将参考QBM使得1.16+的版本也能够使用热同步

使用`!!mirror`可以呼出帮助菜单

使用`!!mirror sync`来进行主世界同步到镜像服

使用`!!mirror start`来开启镜像服

=====Rcon功能=====

**如果你要使用Rcon功能，那么你需要安装一个名为mcrcon的Python依赖库！使用以下命令来安装它**

```bash
$ pip install mcrcon	# Windows用家
$ pip3 install mcrcon	# Linux用家
```

使用`!!mirror info`来查看Rcon配置信息（需要管理员权限）

使用`!!mirror stop`来关闭镜像服（需要rcon功能）

使用`!!mirror status`来查看镜像服是否开启（需要rcon功能）

使用`!!mirror rcon <command>`来对镜像服使用命令（需要管理员权限且此功能需要独立开启，不需要键入`/`）

**请注意，如果你未开启Rcon功能，你无法在主服务器对镜像服进行关闭操作，你必须进入镜像服进行操作！同步的时候请注意镜像服应处于关闭状态！**

如果你想要在服务器中对镜像服进行关闭操作，那么有两种方式，第一种方式即为OP使用`/stop`来关闭服务器，第二种方式则是借助其他的MCDR插件如[SimpleOP](https://github.com/GamerNoTitle/SimpleOP)或者是[StartStopHelper](https://github.com/MCDReforged-Plugins/StartStopHelper)来进行服务器的管理！

如果你发现使用`!!mirror stop`后服务器停在`Waited * seconds attempting force stop`，请你注意，这不是`mirror`插件的bug，这是MC服务器核心的BUG，详情可以看这个地方 https://bugs.mojang.com/browse/MC-154617 

### 初次使用

打开`mirror.json`，进行配置

```json
  {
      "path": "./mirror/",
      "world": ["world"],	
      "command": "python3 MCDReforged.py",
      "delay": 10,
      "remote":{
          "enable": false,
          "address": "127.0.0.1",
          "secret": "password",
          "port": 25575,
          "command": false
      }
  }
```

配置完成后保存即可，现在你就可以打开服务器了并且使用`!!mirror`命令了！

`path` 修改为你的镜像服路径，默认为mirror文件夹

`world` 设置你的世界文件夹，原版只有一个world，spigot类有world,world_nether,world_the_end，根据自己的核心设定，格式为["world","world_nether","..."]

`command` 镜像服启动命令

`delay` 冷回档等待时长

`remote: enable` rcon相关设置，true来打开它

`remote: address` rcon地址，通常在同一台服务器设置为127.0.0.1即可

`remote: secret` rcon密码

`remote: port ` rcon端口

`remote: command` 是否允许使用!!mirror rcon <command>来对镜像服进行指令输入

- [ ] 挖个新坑：区块同步功能
- [ ] 再开个新坑：指定世界同步

---

# English

This is a plugin can help you turn on another mirror server for you to debug or design (**Python3 ONLY**)

> ### 2020/7/6
>
> I've got the problem on the plugin cannot worked well on Minecraft 1.16+ because of the file `Session.lock` have been locked by Minecraft. Now I'm using a compromised solution: turn off the server to copy the world into the mirror one and then turn on the server
>
> I'm trying to refer the QBM plugin to make 1.16+ server can use the hot sync

use `!!mirror` to call out the help menu

use `!!mirror sync` to sync your main world to the mirror server

use `!!mirror start` to open the mirror server

=====Rcon features=====

**When you're using the rcon features, a module called "mcrcon" is required! Use the follow command to install it!**

```bash
$ pip install mcrcon	# Windows Users
$ pip3 install mcrcon	# Linux Users
```

use`!!mirror info` to checkout rcon information(MCDR-Admin permission is required)

use`!!mirror stop` to stop mirror server

use`!!mirror status` to checkout whether the mirror is online or not

use`!!mirror rcon <command>` to input command to mirror server, ***WITHOUT A SLASH AHEAD***

**CAUTION: IF YOU DISABLED THE RCON IN THE MIRROR SERVER, YOU CAN ONLY TWO WAYS TO TURN OFF IT BY USING THE COMMAND `/stop` IN THE MIRROR SERVER OR USE OTHER MCDR PLUGINS LIKE [SimpleOP](https://github.com/GamerNoTitle/SimpleOP) OR [StartStopHelper](https://github.com/MCDReforged-Plugins/StartStopHelper). REMEMBER TO TURN THE MIRROR SERVER OFF BEFORE YOU SYNC THE WORLD INTO IT**

If you found that you stop the server by using the command `!!mirror stop` and it hangs on `Waited * seconds attempting force stop`, I'm very sad to tell you, this is a server-core's bug, not `mirror`‘s. For more information, you can visit here https://bugs.mojang.com/browse/MC-154617 

### Getting Started

Open the file `mirror.json`

Change the configeration in it

```json
  {
      "path": "./mirror/",
      "world": ["world"],
      "command": "python3 MCDReforged.py",
      "delay": 10,
      "remote":{
          "enable": false,
          "address": "127.0.0.1",
          "secret": "password",
          "port": 25575,
          "command": false
      }
  }
```

`path` Your mirror server path, mirror as default

`world` Your world folder(s), the Vanilla server only has the "world" folder but others like spigot has three. Just fill it with your folder(s). The example can be like this -> ["world","world_nether","..."]

`command` The start command for your mirror server

`delay` what time will the cold sync wait before turn off the server

`remote: enable` rcon related settings, true to enable it

`remote: address` rcon address, change it to your address

`remote: secret` rcon password

`remote: port ` rcon port

`remote: command` allow using !!mirror rcon <command> to input command to mirror server