# Postmortem: Disk I/O Saturation Simulation

## Summary
A 60-second disk stress simulation was executed using `stress --hdd 2`. This created sustained disk I/O activity, pushing the system into near 100% disk utilization and high CPU wait time.

## Observations
- `iotop` showed 2 processes writing ~125 MB/s total
- `iostat` showed:
  - 1020 writes/sec on `xvda`
  - ~33ms write latency
  - 98.6% disk utilization
- `dstat` confirmed:
  - 87% CPU waiting on I/O
  - 0% idle
  - No network or read activity

## Tools Used
- `stress`, `iotop`, `iostat`, `dstat`

## Lessons Learned
- Heavy write I/O pushes CPU into wait state
- Disk-bound workloads can starve the CPU of work
- Useful to correlate I/O metrics across tools

## Mitigation (if this were prod)
- Add IOPS monitoring and alerts
- Use faster disk (e.g. NVMe or provisioned IOPS volumes)
- Offload bulk writes to async/background jobs
