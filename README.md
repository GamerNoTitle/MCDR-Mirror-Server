# MCDR-Mirror-Server

[ENGLISH](#English Users)

这是一个能够让你在MCDR的帮助下开镜像服便于调试的插件（仅支持python3）

使用`!!mirror`可以呼出帮助菜单

使用`!!mirror sync`来进行主世界同步到镜像服

使用`!!mirror start`来开启镜像服

请注意，你无法在主服务器对镜像服进行关闭操作，你必须进入镜像服进行操作！同步的时候请注意镜像服应处于关闭状态！

如果你想要在镜像服中对服务器进行操作，那么有两种方式，第一种方式即为OP使用`/stop`来关闭服务器，第二种方式则是借助其他的MCDR插件如[SimpleOP](https://github.com/GamerNoTitle/SimpleOP)或者是[StartStopHelper](https://github.com/MCDReforged-Plugins/StartStopHelper)来进行服务器的管理！

### 初次使用

你需要完成以下操作：

- (可选)设定你的镜像服文件夹，默认为mirror
- 复制整个MCDR服务器到你设置的文件夹内（默认为mirror）
- 配置镜像服的服务器端口
- 配置镜像服的rcon端口
- 打开配置文件`mirror.json`，在`system_type`变量设置自己的系统类型：0为Linux（默认），1为Windows
- 在`server_type`变量设置自己的服务器类型，MC原版服务器及基于其的核心（世界文件夹只有`world`）选择0；Spigot/bukkit类核心（世界文件夹有`world`/`world_nether`/`world_the_end`的）选择1。如果你输入了非法的选项，那么会被当做`Spigot/Bukkit`类处理

目录树大致如下

```
  MCDReforged
  ├─config
  │  ├─mirror.json
  ├─mirror
  │  ├─plugins
  │  │  ├─plugin.py
  │  │  └─...
  │  ├─resources
  │  ├─server
  │  │  └─world
  │  └─utils
  ├─plugins
  │  ├─mirror.py
  │  └─...
  ├─resources
  ├─server
  │  └─world
  └─utils
  
```

---

# English Users

This is a plugin can help you turn on another mirror server for you to debug or design (**Python3 ONLY**)

use `!!mirror` to call out the help menu

use `!!mirror sync` to sync your main world to the mirror server

use `!!mirror start` to open the mirror server

**CAUTIONS: YOU CANNOT DO ANYTHING TO THE MIRROR SERVER WHILE IT'S ONLINE, YOU MUST LOGIN IN THE MIRROR SERVER TO OPERATE IT! WHILE YOU R SYNCING THE SERVER, PLEASE MAKE SURE THE MIRROR SERVER HAS BEEN TURNED OFF**

If you want to turn off or restart the mirror server, there're two ways to do that. The first is that you had become a opreator and use `/stop` to stop it. The Second way is to use other MCDR plugins such as [SimpleOP](https://github.com/GamerNoTitle/SimpleOP) or [StartStopHelper](https://github.com/MCDReforged-Plugins/StartStopHelper) to do it.

### Getting Started

You need to do the following things:

- (Optional) Setting up your mirror server folder at the varible `mirror_folder` (mirror as default)
- Copy all the files in your MCDR (`server` `plugins` etc.) into the mirror folder
- Change the port of the server to another one without conflict
- Change the port of the rcon to another one without conflict if you use it
- Change the rcon port writing in the MCDR config into your setting if you use it
- Open `mirror.json` file, set the `system_type` varible into the type you use (0 for linux as default, 1 for windows)
- Set `server_type` into correct type: Vanilla or Vanilla-Based core like Fabric/Forge that the world folder only has `world` folder please choose `0`, others like Spigot/Bukkit that the world folder has `world`/`world_nether`/`world_the_end` or others please choose `1`. If you type an invalid number it will use `1` as default

Your file should like the following tree

```
  MCDReforged
  ├─config
  │  ├─mirror.json
  ├─mirror
  │  ├─plugins
  │  │  ├─plugin.py
  │  │  └─...
  │  ├─resources
  │  ├─server
  │  │  └─world
  │  └─utils
  ├─plugins
  │  ├─mirror.py
  │  └─...
  ├─resources
  ├─server
  │  └─world
  └─utils
```

