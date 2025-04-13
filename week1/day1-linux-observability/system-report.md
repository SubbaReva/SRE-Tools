===== UPTIME =====
 23:13:59 up 1 day, 18:17,  2 users,  load average: 0.00, 0.00, 0.00

===== TOP CPU PROCESSES =====
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
ubuntu     28257  0.0  0.7  14996  7076 ?        S    22:16   0:02 sshd: ubuntu@pts/1
ubuntu     11968  0.0  0.7  15000  6948 ?        S    21:46   0:00 sshd: ubuntu@pts/0
pcp        27107  0.0  0.7  15376  7552 ?        S    22:11   0:00 /usr/lib/pcp/bin/pmlogger -N -P -d "/var/log/pcp/pmlogger/LOCALHOSTNAME" -r -T24h10m -c config.default -v 100mb -m pmlogger_check %Y%m%d.%H.%M
root       14283  0.0  3.1 1770496 30480 ?       Ssl  22:04   0:00 /usr/lib/snapd/snapd

===== MEMORY USAGE =====
               total        used        free      shared  buff/cache   available
Mem:           957Mi       368Mi       168Mi       936Ki       601Mi       588Mi
Swap:             0B          0B          0B

===== I/O Activity =====
Linux 6.8.0-1024-aws (ip-172-31-10-227) 	04/12/25 	_x86_64_	(1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.06    0.02    0.03    0.02   15.55   84.33

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
loop0            0.00      0.03     0.00   0.00    0.64    23.48    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop1            0.00      0.12     0.00   0.00    0.77    33.52    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop2            0.00      0.01     0.00   0.00    0.84    12.44    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop3            0.00      0.07     0.00   0.00    0.04    31.17    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop4            0.00      0.00     0.00   0.00    0.12     1.88    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
loop5            0.00      0.00     0.00   0.00    0.05     1.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.00
xvda             0.23      7.98     0.07  22.22    0.91    34.30    0.69     23.10     0.52  43.06    1.41    33.45    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.04


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.00    0.00    0.00    0.00    4.76   95.24

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.00    0.00    0.00    0.00    0.00  100.00

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util



===== OPEN TCP PORTS =====
Netid State  Recv-Q Send-Q      Local Address:Port  Peer Address:PortProcess
udp   UNCONN 0      0               127.0.0.1:323        0.0.0.0:*          
udp   UNCONN 0      0              127.0.0.54:53         0.0.0.0:*          
udp   UNCONN 0      0           127.0.0.53%lo:53         0.0.0.0:*          
udp   UNCONN 0      0      172.31.10.227%enX0:68         0.0.0.0:*          
udp   UNCONN 0      0                   [::1]:323           [::]:*          
tcp   LISTEN 0      4096           127.0.0.54:53         0.0.0.0:*          
tcp   LISTEN 0      5                 0.0.0.0:4330       0.0.0.0:*          
tcp   LISTEN 0      5                 0.0.0.0:44321      0.0.0.0:*          
tcp   LISTEN 0      4096        127.0.0.53%lo:53         0.0.0.0:*          
tcp   LISTEN 0      4096                    *:22               *:*          
tcp   LISTEN 0      5                    [::]:4330          [::]:*          
tcp   LISTEN 0      5                    [::]:44321         [::]:*          

===== DISK USAGE =====
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       6.8G  2.3G  4.5G  34% /
tmpfs           479M     0  479M   0% /dev/shm
tmpfs           192M  924K  191M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/xvda16     881M  137M  683M  17% /boot
/dev/xvda15     105M  6.1M   99M   6% /boot/efi
tmpfs            96M   12K   96M   1% /run/user/1000
