# MCDR-Mirror-Server

这是一个能够让你在MCDR的帮助下开镜像服便于调试的插件（仅支持python3）

使用`!!mirror`可以呼出帮助菜单

使用`!!mirror sync`来进行主世界同步到镜像服

使用`!!mirror start`来开启镜像服

请注意，你无法在主服务器对镜像服进行关闭操作，你必须进入镜像服进行操作！同步的时候请注意镜像服应处于关闭状态！

如果你想要在镜像服中对服务器进行操作，那么有两种方式，第一种方式即为OP使用`/stop`来关闭服务器，第二种方式则是借助其他的MCDR插件如[SimpleOP](https://github.com/GamerNoTitle/SimpleOP)或者是[StartStopHelper](https://github.com/MCDReforged-Plugins/StartStopHelper)来进行服务器的管理！

---

### 初次使用

你需要完成以下操作：

- 复制整个MCDR服务器到同目录下的mirror文件夹内
- 配置镜像服的服务器端口
- 配置镜像服的rcon端口
- 打开插件，在`system_type`变量设置自己的系统类型：0为Linux（默认），1为Windows

