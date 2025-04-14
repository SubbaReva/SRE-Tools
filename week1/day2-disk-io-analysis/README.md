I have covered basic disk IO commands that we use to monitor the Disk IO bottlenecks and general disk IO tracing.
Commands used:

1. iotop -o : Shows the top processes with its individual Thread Ids that are making DISK IO. Shows reads and writes size.
2. iostat -xz : Shows each disk level IO stats with its utilization % and wait times etc, Important to check disk utilization percentage.
3. dstat : dashboard that shows CPU, Disk read writes, Network read writes, Paging, etc
4. bpftrace: tool used to trace kernel level or low-level events such as system calls, block I/O events, network packets,s.
5. top: This shows resource utilization status by CPU, Mem, disk with its PIDs (Most frequently used)
