import time
import pyprind

bar = pyprind.ProgBar(100, monitor=True)
for i in range(1000):
    time.sleep(0.05)
    bar.update()
print("Hello")