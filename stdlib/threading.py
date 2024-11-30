# *** threading Reference ***
import threading
import time

# *** Overview ***
# The `threading` module provides a way to run multiple threads (smaller units of execution) in parallel.
# Useful for I/O-bound tasks (e.g., file reading, network requests).
# Threads share memory space, so use locks or other synchronization mechanisms to avoid race conditions.


# *** Thread Class ***
# Create a thread
def worker():
    """Worker thread function."""
    print("Worker is running.")


thread = threading.Thread(target=worker)  # Define the thread
thread.start()  # Start the thread
thread.join()  # Wait for the thread to finish

# Thread attributes
thread.name  # Name of the thread (default is 'Thread-<number>').
thread.ident  # Unique identifier for the thread.
thread.is_alive()  # Check if the thread is still running.

# Daemon Threads
# A daemon thread runs in the background and is killed when the main program exits.
daemon_thread = threading.Thread(target=worker, daemon=True)
daemon_thread.start()

# *** Lock Class ***
# A primitive lock object to synchronize threads.
lock = threading.Lock()

# Acquire and release a lock
lock.acquire()  # Blocks other threads until the lock is released.
# Critical section
lock.release()  # Unlocks, allowing other threads to proceed.

# Use `with` statement for safer lock management
with lock:
    # Critical section
    print("Lock acquired.")

# *** RLock Class ***
# A reentrant lock that allows the same thread to acquire the lock multiple times.
rlock = threading.RLock()
rlock.acquire()
rlock.acquire()  # Reentrant locks allow this.
rlock.release()
rlock.release()

# *** Event Class ***
# An Event object manages a flag that threads can wait for.
event = threading.Event()

# Set, clear, and check the event flag
event.set()  # Set the event flag to True (unblocks waiting threads).
event.clear()  # Reset the flag to False.
event.is_set()  # Check if the flag is True.


# Wait for the event
def wait_for_event():
    print("Waiting for event...")
    event.wait()  # Block until the flag is set.
    print("Event triggered!")


thread = threading.Thread(target=wait_for_event)
thread.start()
time.sleep(1)
event.set()  # Trigger the event.

# *** Semaphore Class ***
# A semaphore limits the number of threads that can access a resource.
semaphore = threading.Semaphore(2)  # Limit to 2 threads at a time.


def limited_access():
    with semaphore:
        print("Resource accessed.")
        time.sleep(1)


threads = [threading.Thread(target=limited_access) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()


# *** Timer Class ***
# Executes a function after a delay.
def delayed_action():
    print("Action executed after delay.")


timer = threading.Timer(5.0, delayed_action)  # Execute after 5 seconds.
timer.start()
timer.cancel()  # Cancel the timer if needed.

# *** ThreadLocal Class ***
# Thread-local storage for data unique to each thread.
thread_local = threading.local()


def thread_task():
    thread_local.data = threading.current_thread().name
    print(f"Thread-local data: {thread_local.data}")


threads = [threading.Thread(target=thread_task) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# *** Utilities ***
# Get the current thread
current_thread = threading.current_thread()
print(current_thread.name)  # MainThread (or a custom name).

# Enumerate all threads
all_threads = threading.enumerate()
print(f"Active threads: {len(all_threads)}")

# Set thread name
thread = threading.Thread(target=worker, name="CustomThread")
thread.start()
print(thread.name)  # CustomThread

# *** Notes ***
# 1. Python threads are limited by the Global Interpreter Lock (GIL), which allows only one thread
#    to execute Python bytecode at a time. Use multiprocessing for CPU-bound tasks.
# 2. Threads are lightweight but not suitable for heavy parallelism. Ideal for I/O-bound tasks.

# Examples:
# - Reading/writing to files or sockets.
# - Waiting for user input or responses from a server.

# Common Debugging Tips:
# - Avoid shared mutable state across threads.
# - Use locks or other synchronization primitives to prevent race conditions.
