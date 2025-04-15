# sim_memory_hog_observable.py
import time

chunk_size = 10_000_000  # ~40MB
chunks = []
max_chunks = 50

print("🚀 Starting memory allocation...")

for i in range(max_chunks):
    try:
        chunks.append([0] * chunk_size)
        print(f"✅ Allocated chunk {i+1}/{max_chunks} (~{(i+1)*40}MB)")
        
        # Give you time to run top and observe
        print("⏸️  Press Enter to allocate next chunk...")
        input()  # <-- you control the pace now

    except MemoryError:
        print(f"❌ MemoryError at chunk {i+1}. Stopping.")
        break

print("⏳ Holding memory for 60 seconds... go wild with /proc, top etc.")
time.sleep(60)

print("✅ Done.")
