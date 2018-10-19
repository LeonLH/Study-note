This file is the note from learning linux from the linux.vbird.org

Wed Sep 26 10:22:37 CST 2018

# Part1. Linux的规划与安装
## Chap2. 主机规划于磁盘分区
1. 第一个分区(512B)：MBR: Master Boot Record(446B) 和 分区表（64B）
	1. 在MBR方式中，主分区只能有4个（64B只能记录8个数据，每组数据包括起始和结尾两个数据），扩展分区(只能有一个)——>逻辑分区(可以有很多)。前四和号码留给主分区和扩展分区，所以逻辑分区的号码从5号开始；
	2. GPT: GUID partition talbe. GPT 分割模式，比原来的MBR分割模式的优点是，MBR的分区表(64)限制，所以最多有4个主分区或扩展分区，而GPT打破这一限制，使得主分区的个数可以多于4。
2. 开机引导程序：
	1. BIOS：CMOS里面记录着主板的电压等的一些信息，按下开机键，BIOS开始运行，首先读取MBR/GPT——> boot loader——>核心档案；
		* 其中，boot loader就是MBR中写入的开机管理程序，它有如下功能：		
			1. 提供选单，就是多重开机的选项；
			2. 转交loader，就是转交给别的loader以用来引导别的系统；
			3. 载入核心档案，就是直接指向开机程序，开始启动OS；
		* boot loader 可以放在MBR或者boot sector中。
	2. UEFI: Unified Extensible Firmware Interface. UEFI搭配GPT开机流程：
		* UEFI 存放在vfat分区内，UEFI 可以直接读取GPT分区表，GPT分区表可以支持更大的位数，所以主分区的个数可以多余4个。读取完分区表找到bootloader之后，流程与上述流程一样。
		* GPT: GUID partition table. GUID, 全球唯一标识符。

Tips:
	1. 挂载：把目录挂在磁盘分区上，要找分区上的内容进入该目录（挂在点）皆可以了。
	2. 磁盘分区：重要的目录单独作为一个分区，这样当根目录坏掉，比如坏轨时，就和以不影响其他分区的资料。以下是比较重要的目录，必要时候可以给他们单独分区：
		* /boot / /home /var Swap

## Chap4. 首次登入与线上求助
Tips: 
	1. <C-d> means End Of INPUT or End Of File, which is equal to quit/exit;
	2. <S-PageUp>/<S-PageDown> means pageup/pagedown in terminal;
	3. `man executivefile` 查看手册，比`executivefile -h/--help` 显示的内容更有可读性, man还可以查看stl容器，比如`man std::vector`；
	4. man page
	```
man -f gdb		//列出命令是gdb的man pages
man -k gdb		//列出有gdb关键字(命令和描述中)的所有man pages

whatis gdb		//相当于man -f
apropos gdb		//相当于man -k
				//上述两个命令，需要有建立whatis资料库才行，这需要root身份
mandb			//建立whatis资料库(以root身份)

	```
	5. info page, 类似于文字模式的网页显示资料，有类似超链接的节点
	```
info gdb		//进入info页面，进入之后，N-next，P-previous，U-up

	```
		* TAB---next hypertext link				RET---into current link
		* l-----go back to last node			1...9-pick the 1st-9th item in this node's menu
		* C-g---cancel the current operation	H-----get/quit help
	6. 资料同步写入硬盘---sync

# Part2 Linux文件/目录与硬盘格式
## Chap6. Linux文件权限于目录配置
1. 所有者/所属组/密码的记录文件：
	1. /etc/passwd		记录的是账号
	2. /etc/shadow		记录的是密码
	3. /etc/group		记录的是群组
2. 权限相关命令：
	1. chgrp	改变文件所属组, -R递归
	2. chown	改变文件所有者, -R递归, 可以同时修改所有者和所属组两个信息，`chown ownername:groupname filename`
	3. chmod	改变文件的权限, SUID，SGID，SBIT
		* `chmod 644 filename`
		* `chmod u/g/o/a  +/-/= r/w/x`
3. 目录的写权限，是对目录清单进行修改的权限，即新建/删除/重命名/移动文件的权；目录的执行权限，是是否可以进入该目录；

Tips
1. 为什么没有写权限的人，还是可以通过强制执行写入内容，只是写之后，文件的所有者变为了执行该操作的人？ 是因为没有写权限，强制写入时，vim会删除原文件，重建同名的文件，然后把内容写入，但是写入之后文件的所有者和所属组就都变成了执行该强制操作的人了。如果不希望此文件被写入或修改，可以将拥有该文件的目录的写权限对操作者禁止，别人删除不了文件也添加不了文件了，也不会发生上述情况。
2. Linux中的文件是否可以执行和它的文件名没有关系(windows 是用扩展名.exe或其他扩展名来判断文件是否可以执行), Linux中是用x这个权限来判断文件是否时可执行文件的。

4. FHS(Filesystem hierarchy standard)
	1. `/` :与开机系统有关；
	2. `/usr`: (unix software resource)与软件安装/执行有关；
	3. `/var`:（variable）与系统运行过程有关；

##Chap6 Linux档案与目录管理
1. 几个命令
```
head/tail		//取出前几行/后几行
od 				//非纯文字文件
cat/tac/nl 		//nl添加行号
```
2. 几种时间
```
modification time (mtime) 		//内容资料变更时改变
status time (ctime) 			//权限属性变更时改变
access time (atime) 			//被访问后改变
touch d/t/a						//修改上述三种时间
```
3. 预设权限与隐藏属性  
```
umask 			//预设权限需要减掉的权限值
chattr			//设定文件隐藏属性
lsattr			//显示文件隐藏属性
```
4. 特殊权限, SUID, SGID, SBIT, 相当于在原本的x权限上提升。
	1. SUID s权限
		* SUID仅对二进制文件有效；
		* 执行者对该文件要有x权限；
		* 本权限仅在程序的执行过程中有效；
		* 程序执行过程中，执行者的权限会变成owner的权限；
	2. SGID s权限
		* 用于文件时：
		* SGID仅对二进制文件有效；
		* 执行者对该文件要有x权限；
		* 本权限仅在程序的执行过程中有效；
		* 程序执行过程中，执行这权限会变成group的权限；

		* 用于目录时：
		* 用途：使用者在本目录有w权限，则使用这在该目录下新建的文件的所属组和目录的所属组相同；
	3. SBIT (Sticky Bit) ，仅对目录有效。
		* 当使用者对此目录具有w和x权限时，使用在该目录下新建的文件/目录，仅有自己和root可以删除；
5. 查看文件属性：`file`
6. 搜索文件
	1. `which executablefile`, -a ;		//可执行文件
	2. `whereis filename`, [-lbmsu];	//在特定目录中寻赵文件 
	3. `locate [-iclSr];				//在/var/lib/mlocate资料库中查找，带有关键字的资料，可用`updatedb`来更新资料库；
	4. `find`,超级强大，可以加各种参数来限定查找的文件属性/user/size/权限等，但它是硬扫描，所以时间较慢；

##Chap7 磁盘与文件系统
1. ext2/ext3/ext4, 从ext3开始支持文件日志功能
	1. Block Group ---> SuperBlock ---> inode + block
	2. `dumpe2fs` 查看文件系统的描述资料 
	3. `blkid` 列出UUID
	4. `e2fsck` 一致性检查
2. xfs 不需要预先格式化, inode/block 是在使用的过程中动态产生。
	1. `xfs_info` 查看文件系统的描述资料
3. 硬盘与目录的容量du/df
	1. `df` 列出文件系统的整体硬盘使用量, 对象是disk；
	2. `du` 评估文件系统的硬盘施用量, 对象是file；
4. ln 可以做硬链接(hard link)/软链接(symbolic link)
	1. hard link 实际上就是在目录的block中写入文件名和文件的inode，一般不会造成空间减小，它不可以对目录操作；
	2. symbolic link 是新建了inode和block，内容相当于文件的绝对路径，它可以看成是windows下的快捷方式，它不可以对目录操作。  
5. 硬盘分区：
	1. `lsblk` 列出系统上的所有硬盘列表
	2. `blkid` 列出UUID
	3. `parted` 列出硬盘的分区类型和分区信息
	4. 分区：gdisk(for GPT)/fdisk(for MBR)
	5. `partprobe` 更新Linux核心的分区信息(/proc/partitions), 避免重启；
	6. `mkfs` make filesystem 综合指令，具体哪种文件系统，还需要进一步确定，使用对应的指令，如`mkfs.xfs` `mkfs.ext4`,etc. 
6. 文件系统检验
	1. `xfs_repair` 处理XFS文件系统；
	2. `fsck.ext4` 处理EXT4文件系统；
7. 挂载与卸载 mount/umount
	1. 开机自动挂载，实际上就是在/etc/fstab文件中写入特定的分区信息，开机的时候，系统会检查fstab，根据它来挂载。此外，使用`mount -a`也会根据/etc/fstab来挂载；
	2. 挂载DVD映象文件, `mount -o loop /tmp/CentOS-7.0-14.06_64-DVD.iso /data/centos_dvd`, 利用`mount loop`; 
	3. 制作loop文件，并将loop格式化为文件系统，最后将它挂载，这样就类似于一个新的分区(实际上不是, 只是loop文件); 
	```
	dd if=/dev/zero of=/srv/loopdev bs=1M count=512		//建立一个大块
	mkfs.xfs -f /srv/loopdev							//格式化
	blkid /srv/loopdev
	mount -o loop UUID="xxx" /mnt 						//挂载
	df /mnt
	```

8. 不论分区表是GPT还是MBR都可以进行分区的工具，`parted` 它是非非交互式的，而fdisk/gdisk是交互式的，所以parted可以用来脚本文件中一次性建立很多分区；

## Chap8 文件的压缩与打包
1. 压缩文档的格式： *.tar, *.tar.gz, *.tgz, *.gz, *.Z, *.bz2, *.xz; 
2. 压缩软件： gzip, bzip2, xz, 打包： tar; 
	1. gzip, -d 解压, zcat/zmore/zless/zgrep无需解压对压缩文件操作;
	2. bzip2,-d 解压, bzcat/bzmore/bzless/bzgrep, 同上；
	3. xz,   -d 解压，xzcat/xzmore/xzless/xzgrep, 同上；
	4. tar 打包：
		* 压缩：			`tar -jcv -f filename`;
		* 查看tar包中文件：	`tar -jtv -f filename.tar.bz2`;
		* 解压：			`tar -jxv -f filename.tar.bz2` -C directoryname`;
		* 上述j代表bz，可换为z/J，z代表gzip，J代表xz, 主要差异是在压缩比和时间上，一般来说，压缩比越大，时间越长；
		```
time tar -zpcv -f /root/etc.tar.gz  /etc
time tar -jpcv -f /root/etc.tar.bz2 /etc
time tar -Jpcv -f /root/etc.tar.xz  /etc 
		```
		* 仅解压tar压缩包中单个文件：
		```
tar -jtv -f /root/etc.tar.bz2 |grep 'shadow'	//查看包含shadow的文件
tar -jxv -f /root/etc.tar.bz2 etc/shadow 		//解压单个文件
		```
		* 几个参数：
			不包含某个目录：--exclude=filename(可以有路径)
			仅备份比某时刻更新的文件：--newer-mtime --newer(包含mtime和ctime)
			将资料流一边打包一边压缩到目标目录里去

3. 文件系统的备份与还原(xfs文件系统为例)
	1. 备份：xfsdump, 累计备份(incremental backups)
	2. 还原：xfsrestore
4. 制作映像文件
	1. 普通iso文件：	`mkisofs`
	2. 可开机ios文件：
	3. 光碟烧录工具：	`cdrecord/wodim`
5. 其他压缩与备份工具：
	1. dd, 可以将磁盘上的superblock/boot sector/meta data通通复制到目标文件中，因此不需要格式化。可以用来完整的备份磁盘。
`dd if="input_file" of="output_file" bs="block_size" count="number"`
	
	2. cpio, 相当优秀的备份指令，不过需要搭配find类似指令读入要备份的文件名：
	```
cpio -ovcB  > [file|device] 		//备份
cpio -ivcdu < [file|device]			//还原
cpio -ivct  < [file|device] 		//查看
	```

PS:  
	1. `time` 可以列出命令运行时间；


##Chap9 vim
1. dos2unix/unix2dos, DOS下换行是CRLF，Linux下是LF，所以需要转换。


##Chap10 认识与学习BASH
1. alias lm='ls -al' How to make it work every time restart host? 
2. 显示变量：`echo $variablename` 
3. 变量设定规则：
	1. =； 
	2. =两端不能有空格；
	3. 开头不能是空格；
	4. 单引号/双引号：
		* 双引号保留原特性,具有变量置换功能；
		* 单引号内仅仅是字符串，不具有变量置换功能；
	5. \ 转义字符将特殊符号变为普通符号；
	6. `指令` 或 $(指令) 可以返回指令的结果, 例如：
	```
		version=$(uname -r)
		或 version=`uname -r`
	```
	7. 扩增变量内容，用 "$变量名" 或 ${变量}, 例如：
		`PATH="$PATH":/home/bin` 或 `PATH=${PATH}:/home/bin`
	8. 以export把变量变成环境变量：`export PATH`;
	9. 大写系统变量，小写自定义变量；
	10. 取消变量：`unset variablename`;
4. 列出
	1. env 列出环境变量；
	2. set 列出所有变量；
	3. 子进程会继承父进程的环境遍历，但不会继承父进程的自定义变量，此时就可以使用，`export  variablename` 来把自己的变量分享给后来调用的子进程。而且设置完成后，关于语系的设定还是要，好好学习操作一番才能理解，暂时不用着急着设定成为中文。另外，要熟练英文的书写，多练习，慢慢地要有用英文书写交流的能力，不改成中文也可以比较好的英文学习环境。
5. 变量的读取/数组/声明；
	1. `read [-tp] variable`				//读取变量
	2. `declare/typeset [-aixr] variable`	//声明变量类型, -/+x可以设定取消成为环境变量，-r只读，-p可以列出
6. 限定bash使用者使用的资源(可打开的文件数/大小，CPU，RAM)，ulimit:
7. 变量的删除/取代/替换：
	1. 删除：`${variable#/*local/bin}`;		// # 表示从左到右删除最短的那个相匹配的，## 表示从左到右删除最长的匹配的，%/%% 表示从右到左删除最短/最长的
	2. 取代：`echo ${path/sbin/SBIN}`;		// 如果path和sbin之间是两条斜线，则所有符合的条件都会被取代
	3. 判断设定默认值：
	```
`username=${username-root}`		// 如果没有被设定则username默认为root
`username=${username:-root}`	// 变量为空或者未设定，都以默认为值
	```
8. 别名, 别名的设定与变量的设定基本是一样的
	1. `alias aliasname=command`		//set alias
	2. `unalias aliasname`				//unset alias
9. 历史命令 history
	1. `!command` 由最近的指令开始向上搜索第一个以command开头的指令并执行；
10. Login-shell, Load after login with tty1-tty6. Non-login shell load by exist bash calling. 
11. Ubuntu's directory is a little different from CentOS's, so if you don't find files in ubuntu which it exist in CentOS, Try `ls | grep keyword` and then read the relative manual. 
12. Configuration of bash:
	1. /etc/profile /etc/profile.d/ /etc/locale.conf
	2. ~/.bash_profile  ~/.bash_login ~/.bashrc /etc/bashrc ~/.profile
	3. `source conf_file` loading the configuration
13. Login-shell will read above file as sequence, Non-login-shell will only load the ~/.bashrc
14. Put the right info and error info into one file by using `2>&1 file` or `&>`;
15. 管道符后面的指令是要能接收 standard input 才可以，例如，less/more/head/tail
16. 一些常用工具：
	* cut  -d|-f|-c ;						//截断
	* grep -a|-c|-i|-n|-v|--color=auto ; 	//筛选
	* sort -f|-b|-M|-n|-r|-u|-t|-k ;		//排序
	* uniq -i|-c ;							//去重
	* wc   -l|-w|-m ;						//统计
	* tee  -a ;								//双向重定向
17. 字元转换命令：
	* tr   -d|-s SET1; 						//删除或替换
	* col  -x|-b 							//TAB->空白
	* join -t|-i|-1|-2; 					//合并两个有相关性的文本
	* paste -d file1 file2; 				//直接粘贴在后面，TAB隔开
	* expand -t 							//TAB->N个空白
	* split -b|-l file PREFIX				//分割文件
	* xargs -O|-e|-p|-n command				//把文本分隔处理后，传给命令，可以实现一次传一个(几个)参数给名令
	* 减号 - 某些命令中可以代替stdin和stdout




























Note:
> type -a ls 		// 查看ls的指令执行顺序
>
> /etc/issue 中记录着，登陆之前显示的信息，可以修改成各种格式（如，时间，本机版本等）;
>
> /etc/motd 记录着上述类似信息，只不过是出现在远程登陆端的显示界面上；





---
Above 10.5.2
 


