# --coding: utf-8 --
import RPi.GPIO as GPIO
import time
from ultrasonic import distance
GPIO.setmode(GPIO.BCM)
#定义 GPIO 引脚

GPIO_IN1 = 14
GPIO_IN2 = 15
GPIO_IN3 = 18
GPIO_IN4 = 23

GPIO.setwarnings(False)
GPIO.setup(GPIO_IN1, GPIO.OUT)
GPIO.setup(GPIO_IN2, GPIO.OUT)
GPIO.setup(GPIO_IN3, GPIO.OUT)
GPIO.setup(GPIO_IN4, GPIO.OUT)

GPIO.output(GPIO_IN1,False)
GPIO.output(GPIO_IN2,True)
GPIO.output(GPIO_IN3,True)
GPIO.output(GPIO_IN4,False)

p1 = GPIO.PWM(GPIO_IN2, 200) # channel=? frequency=50Hz（需要修改高电平引脚）
p2 = GPIO.PWM(GPIO_IN3, 200) # channel=? frequency=50Hz（需要修改高电平引脚）
p1.start(40) #to start PWM
p2.start(50)
# def turnLeft(distance):
#     if distance <= 5:

try:
    while 1:
        dist = distance()
        print("Measured Distance = {:.2f} cm".format(dist))
        time.sleep(1)



# Reset by pressing CTRL + C
except KeyboardInterrupt:
    p1.stop()
    p2.stop()
    print("Measurement stopped by User")
    GPIO.cleanup()
