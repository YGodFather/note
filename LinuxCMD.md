1、查看网关：
# netstat -rn   or  route -n
2、修改网址为静态网址
# /etc/network/interfaces

3、查看CPU型号
 # cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
 
 4、查看系统内核
 # uname -a
 
