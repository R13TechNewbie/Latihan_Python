import os
import sys

x, y = os.popen("stty size", "r").read().split()
height = int(x)
width = int(y)
print("=" * width)
print(height, width)
print("=" * width)

sys.stdout.write("\rTest 1")
sys.stdout.flush()
os.system("sleep 1")
sys.stdout.write("\rTest 2")
sys.stdout.flush()
os.system("sleep 1")
sys.stdout.write("\rTest 3")
sys.stdout.flush()
os.system("sleep 1")
sys.stdout.write("\rTest 4")
sys.stdout.flush()