[Description]
This is the note of the buffer overflow class.  
  
[Environment]
> $ uname -a  
> Linux ubuntu 3.19.0-25-generic #26~14.04.1-Ubuntu SMP Fri Jul 24 21:18:00 UTC 2015 i686 i686 i686 GNU/Linux  
   
> $ cat /etc/*-release  
> DISTRIB_ID=Ubuntu  
> DISTRIB_RELEASE=14.04  
> DISTRIB_CODENAME=trusty  
> DISTRIB_DESCRIPTION="Ubuntu 14.04.3 LTS"  
> NAME="Ubuntu"  
> VERSION="14.04.3 LTS, Trusty Tahr"  
> ID=ubuntu  
> ID_LIKE=debian  
> PRETTY_NAME="Ubuntu 14.04.3 LTS"  
> VERSION_ID="14.04"  
> HOME_URL="http://www.ubuntu.com/"  
> SUPPORT_URL="http://help.ubuntu.com/"  
> BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"  
  
[Compilations]  
 * With ASLR, Stack protector, DEP, TURNED OFF  
   gcc -fno-stack-protector -z execstack bof.c -o bof  
   sudo sysctl -w kernel.randomize_va_space=0  
  
[Usage]  
./bof AAAA  
./bof \`python -c 'print "A" * 212 + "BBBB" + "C" * 100'\`  
./bof \`python sploit.py\`  
./bof \`python sploit2.py\`  
  
[gdb cheatsheets]  
http://darkdust.net/files/GDB%20Cheat%20Sheet.pdf  
start debugging with gdb  
`gdb -q bof`  

run program inside gdb with input from python script  
`r \`python sploit.py\``  

print out sharedlibrary  
`info sharedlibrary`  

find jump esp command in between addr1 and addr2  
`find /b addr1, addr2, 0xff, 0xe4`  

print out process mapping  
`info proc map`  

print out the current register  
`i r`  

print out 20 Words (four bytes) specified in address  
`x/20x address`  

print out 5 instructions specified in address  
`x/5i address`  

set breakpoints in address  
`b * address`  
  
[Tools]  
readelf  
`readelf -a bof | grep WA`  

ROPgadget: https://github.com/JonathanSalwan/ROPgadget  
`ROPgadget --binary /lib/i386-linux-gnu/libc-2.19.so > libc`  
`cat libc | grep ": inc eax ; ret"`  
  
