# MCDR-Mirror-Server

如果你正在使用MCDR 0.x，请使用[Below-1.0分支](https://github.com/GamerNoTitle/MCDR-Mirror-Server/tree/Below-1.0)下的插件/If you're using MCDR 0.x, please use the plugin on [Below-1.0 Branch](https://github.com/GamerNoTitle/MCDR-Mirror-Server/tree/Below-1.0)

[ENGLISH](#English)

**MCDR1.0+的rcon功能还没适配，所以加载时会报错，不过不影响使用（大概），如果你对rcon功能有要求请看[这里](https://github.com/GamerNoTitle/MCDR-Mirror-Server/tree/Below-1.0)**

这是一个能够让你在MCDR的帮助下开镜像服便于调试的插件（仅支持python3），现已支持1.16+。如果你不懂怎么使用，可以看[这里的例子](https://bili33.top/2020/07/18/MCDR-Mirror-Server-Usage/)

使用`!!mirror`可以呼出帮助菜单

使用`!!mirror sync`来进行主世界同步到镜像服

使用`!!mirror start`来开启镜像服

=====Rcon功能=====

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

`command` 镜像服启动命令，[Windows用户请点我看注意事项](#启动命令Windows用户)

`remote: enable` rcon相关设置，true来打开它

`remote: address` rcon地址，通常在同一台服务器设置为127.0.0.1即可

`remote: secret` rcon密码

`remote: port ` rcon端口

`remote: command` 是否允许使用!!mirror rcon \<command>来对镜像服进行指令输入

赞助：[爱发电](https://afdian.net/@GamerNoTitle)

### 启动命令：Windows用户

在Windows中，推荐直接写好一个bat文件，然后用绝对路径调用bat文件

例如，我的bat文件如下

```batch
java -Xmx4G -jar server.jar
```

命名为`mirrorstart.bat`，文件放在`D:\MinecraftServer`，那我只需要把启动命令改成`D:\MincraftServer\mirrorstart.bat`即可，这么操作是为了能够直接打开一个新的命令窗口，避免关闭镜像服的时候把主服务器也关掉了

---

# English

**This plugin has not adapted to rcon function in MCDR1.0+ yet, if you have the requirement of the rcon function, please visit [here](https://github.com/GamerNoTitle/MCDR-Mirror-Server/tree/Below-1.0) **

This is a plugin can help you turn on another mirror server for you to debug or design (**Python3 ONLY**), now supported Minecraft 1.16+

If you don't know how to use it, you can go [here and check the example](https://bili33.top/2020/07/18/MCDR-Mirror-Server-Usage/#English)

use `!!mirror` to call out the help menu

use `!!mirror sync` to sync your main world to the mirror server

use `!!mirror start` to open the mirror server

=====Rcon features=====

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

`command` The start command for your mirror server [(Windows Users should click me and read for more information)](#Windows Users Start Command)

`remote: enable` rcon related settings, true to enable it

`remote: address` rcon address, change it to your address

`remote: secret` rcon password

`remote: port ` rcon port

`remote: command` allow using !!mirror rcon <command> to input command to mirror server

Donate：[aifadian](https://afdian.net/@GamerNoTitle) | [Paypal](https://paypal.me/GamerNoTitle)

### Windows Users: Start command

In Windows environment, I recommand that you write a batch file and put it in where you will use to open your mirror server, and use the absolute path to open the file

for example, i have a batch file like this

```batch
java -Xmx4G -jar server.jar
```

the file named `mirrorstart.bat` and placed in the path `D:\MinecraftServer` , then the start command shoule be `D:\MincraftServer\mirrorstart.bat`

In order to open a new shell window to avoid the main server being killed when you close your mirror server by rcon, i really recommand you do so!
