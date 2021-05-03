import rotatescreen
import time
rotate = rotatescreen.get_primary_display()
rotate.rotate_to(0)
for i in range(20):
    time.sleep(1)
    rotate.rotate_to(i*90%360)
 
