1、查看网关：

# netstat -rn   or  route -n
2、修改网址为静态网址
# /etc/network/interfaces

auto p8p1
iface p8p1 inet static
address 10.10.1.31
gateway 10.10.1.200
netmask 255.255.255.0



3、查看CPU型号

 # cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c

 4、查看系统内核
 # uname -a

5、grep命令 

grep -C 5 foo file 显示file文件里匹配foo字串那行以及上下5行
grep -B 5 foo file 显示foo及前5行
grep -A 5 foo file 显示foo及后5行 