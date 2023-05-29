

[influxdb2.1安装](https://www.atla.top/a/13.html)
[对RFC 3339的时间、时区格式详解](https://www.jianshu.com/p/f50005a2410c)
[Python字符串格式化--format()方法](https://blog.csdn.net/i_chaoren/article/details/77922939)


命令:
查看软件版本  sudo apt-cache madison influxdb

Windows配置wsl 端口转发：
netsh interface portproxy add v4tov4 listenport=8086 connectaddress= 172.17.24.66 connectport=8086 listenaddress=* protocol=tcp
netsh interface portproxy delete v4tov4 listenport=80 protocol=tcp

安装ifconfig/netstat网络工具 (net-tools工具箱包括arp, hostname, ifconfig, netstat, rarp, route, plipconfig, slattach, mii-tool and iptunnel and ipmaddr等命令)
apt-get install net-tools


