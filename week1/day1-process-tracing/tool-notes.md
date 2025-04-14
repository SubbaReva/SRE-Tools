The strace command is tracing the syscalls that are made by that command
For example when I ran strace on curl that I made to google.com

It displayed all the syscalls in order to fetch the data from server 
ex: execc() call, receive() call etc are made.



Notes:
strace intercepts syscalls between a process and the Linux kernel.
It lets you see exactly what a process is doing behind the scenes — from opening files to connecting to networks to sleeping and dying.

So I used strace to trace a process like ping google.com
It was using various system calls but mainly
recvmsg(), sendto(), write(), poll(), clock_gettime() 
These are basically the things that linux is running on its kernal to ping a website.

