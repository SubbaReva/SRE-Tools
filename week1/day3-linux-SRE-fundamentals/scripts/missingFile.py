# sim_failing_file.py
print("Opening a non-existent file...")
with open("/tmp/definitely_not_here.txt", "r") as f:
    data = f.read()
    sleep(100)
print("This won't print.")
