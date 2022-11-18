from house import House
import time
import os

def animate():
    for i in range(3,38):
        os.system('cls')
        house = House(i, chr(i+33), chr(127-i))
        house.draw()
        time.sleep(0.3)

animate()