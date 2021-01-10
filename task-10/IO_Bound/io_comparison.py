import os

print("IO-Bound comparison:")
os.system("python io_non_concurrent.py")
os.system("python io_threading.py")
os.system("python io_mp.py")
