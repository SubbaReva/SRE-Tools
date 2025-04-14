/proc/$$ - The proc folder stores all details about the system wide processes. $$ is for bash process 

cat status - This file has the process metadata (note: ps command would fetch all details of process from here)
               ex: Name, state, Pid, VmSize etc

ls fd - This command shows the file descriptors currently opened by the process.
        ex: 0, 1, 2 = stdin, stdout, stderr

cat sched - This shows scheduling stats for the process. It’s way deeper than top.
Key fields:
	•	se.exec_start: total runtime in nanoseconds
	•	nr_voluntary_switches: how many times it yielded CPU willingly
	•	nr_involuntary_switches: how many times it got booted off
	•	se.sum_exec_runtime: how much CPU time it’s actually gotten
	•	nr_migrations: how many times it’s been moved across cores


limit - This shows resource limits (rlimits) for the process.
Common fields:
	•	Max cpu time: max time allowed before process gets killed
	•	Max file size: limit for file output size
	•	Max data size: heap size (malloc)
	•	Max open files: ulimit -n equivalent
	•	Max locked memory: how much memory can be locked (e.g., for mlock)
	•	Max processes: max number of forks allowed

🧠 SRE Insight:

OOM events? Too many open files? This is your first stop. If a process dies under load, this file often holds the smoking gun.

