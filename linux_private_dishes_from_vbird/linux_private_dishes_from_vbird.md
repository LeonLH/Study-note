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
## Chap1. Linux文件权限于目录配置


---
