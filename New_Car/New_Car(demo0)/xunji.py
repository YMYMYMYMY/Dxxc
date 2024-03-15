import RPi.GPIO as GPIO
import serial
import time
# 串口设备名称
serial_port = '/dev/ttyACM0'

# 打开串口连接
ser = serial.Serial(serial_port, 115200)  # 根据需要设置波特率

#ser.open()
# 发送二进制代码
#binary_code = b'\x7B\x00\x00\x0F\x00\x00\x00\x00\x00\x74\x7D'  # 要发送的二进制代码

#ser.write(binary_code)


# 关闭串口连接
def runn(binary_code):
  ser = serial.Serial(serial_port, 115200)
  ser.write(binary_code)
  ser.close()

def run():
    ser = serial.Serial(serial_port, 115200)
    binary_code_run = b'\x7B\x00\x00\x0F\x00\x00\x00\x00\x00\x74\x7D'
    ser.write(binary_code_run)
    ser.close()
    return

def back():
    ser = serial.Serial(serial_port, 115200)
    binary_code_back = b'\x7B\x00\x00\xF1\x00\x00\x00\x00\x00\x8A\x7D'
    ser.write(binary_code_back)
    ser.close()
    return

def stop():
    ser = serial.Serial(serial_port, 115200)
    binary_code_stop = b'\x7B\x00\x00\x00\x00\x00\x00\x00\x00\x7B\x7D'
    ser.write(binary_code_stop)
    ser.close()
    return

def left():
    ser = serial.Serial(serial_port, 115200)
    binary_code_left = b'\x7B\x00\x00\x00\x00\x00\x00\x0F\x00\x74\x7D'
    ser.write(binary_code_left)
    ser.close()
    return

def right():
    ser = serial.Serial(serial_port, 115200)
    binary_code_left = b'\x7B\x00\x00\x00\x00\x00\x00\xF1\x00\x8A\x7D'
    ser.write(binary_code_left)
    ser.close()
    return


Tracking_1 = 11
Tracking_2 = 13
Tracking_3 = 15
Tracking_4 = 29
Tracking_5 = 31
Tracking_6 = 33
Tracking_7 = 35
Tracking_8 = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


#
GPIO.setup(Tracking_1, GPIO.IN)
GPIO.setup(Tracking_2, GPIO.IN)
GPIO.setup(Tracking_3, GPIO.IN)
GPIO.setup(Tracking_4, GPIO.IN)
GPIO.setup(Tracking_5, GPIO.IN)
GPIO.setup(Tracking_6, GPIO.IN)
GPIO.setup(Tracking_7, GPIO.IN)
GPIO.setup(Tracking_8, GPIO.IN)

while(0):
    
    GPIO.setup(Tracking_1, GPIO.IN)
    GPIO.setup(Tracking_2, GPIO.IN)
    GPIO.setup(Tracking_3, GPIO.IN)
    GPIO.setup(Tracking_4, GPIO.IN)
    GPIO.setup(Tracking_5, GPIO.IN)
    GPIO.setup(Tracking_6, GPIO.IN)
    GPIO.setup(Tracking_7, GPIO.IN)
    GPIO.setup(Tracking_8, GPIO.IN)
    
    Tracking_1Value = GPIO.input(Tracking_1)
    Tracking_2Value = GPIO.input(Tracking_2)
    Tracking_3Value = GPIO.input(Tracking_3)
    Tracking_4Value = GPIO.input(Tracking_4)
    Tracking_5Value = GPIO.input(Tracking_5)
    Tracking_6Value = GPIO.input(Tracking_6)
    Tracking_7Value = GPIO.input(Tracking_7)
    Tracking_8Value = GPIO.input(Tracking_8)

    print(Tracking_1Value,Tracking_2Value,Tracking_3Value,Tracking_4Value,Tracking_5Value,Tracking_6Value,Tracking_7Value,Tracking_8Value)


def tracking_function1():
    #接收输入信号
    Tracking_1Value = GPIO.input(Tracking_1)
    Tracking_2Value = GPIO.input(Tracking_2)
    Tracking_3Value = GPIO.input(Tracking_3)
    Tracking_4Value = GPIO.input(Tracking_4)
    Tracking_5Value = GPIO.input(Tracking_5)
    Tracking_6Value = GPIO.input(Tracking_6)
    Tracking_7Value = GPIO.input(Tracking_7)
    Tracking_8Value = GPIO.input(Tracking_8)

#
    #print(Tracking_Left1Value, Tracking_Left2Value, Tracking_Right1Value, Tracking_Right2Value)
    #四路循迹引脚电平状态
    #1 0 0 0
    #1 1 0 0
    #处理右直角的转动
    if ((Tracking_1Value == 1 or Tracking_2Value == 1) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 0 or Tracking_6Value == 0 )and (Tracking_7Value == 0 or Tracking_8Value == 0 ))or ((Tracking_1Value == 1 or Tracking_2Value == 1) and ( Tracking_3Value == 1 or Tracking_4Value == 1 )and (Tracking_5Value == 0 or Tracking_6Value == 0 )
            and (Tracking_7Value == 0 or Tracking_8Value == 0 )\
            ):
        right()
        time.sleep(0.28)
#
    #四路循迹引脚电平状态
    #0 0 0 1
    #0 0 1 1
    #处理左直角的转动
    elif ((Tracking_1Value == 0 or Tracking_2Value == 0) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 0 or Tracking_6Value == 0 )and (Tracking_7Value == 1 or Tracking_8Value == 1 ))or ((Tracking_1Value == 0 or Tracking_2Value == 0) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 1 or Tracking_6Value == 1 )
            and (Tracking_7Value == 1 or Tracking_8Value == 1 )\
            ):
        left()
        time.sleep(0.28)
#
    #四路循迹引脚电平状态
    #0 0 0 0
    #处理丁字口的转动
    elif (Tracking_1Value == 0 or Tracking_2Value == 0) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 0 or Tracking_6Value == 0 )and (Tracking_7Value == 0 or Tracking_8Value == 0 ):
        right()
        time.sleep(0.28)
#
    #四路循迹引脚电平状态
    #1 0 1 1
    #0 1 1 1
    #处理左小弯
    elif ((Tracking_1Value == 1 or Tracking_2Value == 1) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 1 or Tracking_6Value == 1 )and (Tracking_7Value == 1 or Tracking_8Value == 1 ))or ((Tracking_1Value == 0 or Tracking_2Value == 0) and ( Tracking_3Value == 1 or Tracking_4Value == 1 )and (Tracking_5Value == 1 or Tracking_6Value == 1 )
            and (Tracking_7Value == 1 or Tracking_8Value == 1 )\
            ):
        left()
        time.sleep(0.03)
    #四路循迹引脚电平状态
    #1 1 0 1
    #1 1 1 0
    #处理右小弯
    elif ((Tracking_1Value == 1 or Tracking_2Value == 1) and ( Tracking_3Value == 1 or Tracking_4Value == 1 )and (Tracking_5Value == 0 or Tracking_6Value == 0 )and (Tracking_7Value == 1 or Tracking_8Value == 1 ))or ((Tracking_1Value == 1 or Tracking_2Value == 1) and ( Tracking_3Value == 1 or Tracking_4Value == 1 )and (Tracking_5Value == 1 or Tracking_6Value == 1 )
            and (Tracking_7Value == 0 or Tracking_8Value == 0 )\
            ):
        right()
        time.sleep(0.03)
#
    #四路循迹引脚电平状态
    #1 0 0 1
    #处理直线
    elif ((Tracking_1Value == 0 or Tracking_2Value == 0) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 0 or Tracking_6Value == 0 )and (Tracking_7Value == 1 or Tracking_8Value == 1 ))or ((Tracking_1Value == 0 or Tracking_2Value == 0) and ( Tracking_3Value == 0 or Tracking_4Value == 0 )and (Tracking_5Value == 1 or Tracking_6Value == 1 )
            and (Tracking_7Value == 1 or Tracking_8Value == 1 )\
            ):
        run()
        time.sleep(0.01)
#
    #当为1 1 1 1时小车直行

#elif Tracking_Left1Value == 1 and Tracking_Left2Value == 1 and Tracking_Right1Value == 1 and Tracking_Right2Value == 1:

#car.Car_Run(65, 65)
#        time.sleep(0.01)

while(1):
    tracking_function1()
stop()
