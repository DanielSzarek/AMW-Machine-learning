import os

print("Images comparison:")
os.system("python images_non_concurrent.py")
os.system("python images_threading.py")
os.system("python images_mp.py")
