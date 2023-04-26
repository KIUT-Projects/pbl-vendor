import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
 
# I2C busni yaratish
i2c = busio.I2C(board.SCL, board.SDA)

# ADS1115 obyektini yaratish
ads = ADS.ADS1115(i2c)

# Pin tanlash
chan = AnalogIn(ads, ADS.P1)

# Maksimum va minimum voltajni aniqlash
MAX_VALUE = 2.9710
MIN_VALUE = 1.7650

kop=100
ortacha=50
kam=20

def convert_voltage_to_percentage_and_liters(voltage):
    percentage = 100 - ((voltage - MIN_VALUE) / (MAX_VALUE - MIN_VALUE) * 100.0)
    liters = 450-((voltage - MIN_VALUE) / (MAX_VALUE - MIN_VALUE) * 450)
    return percentage, liters


while True:
    # Analog ma'lumot olish
    voltage = chan.voltage
    persi=0


    # Ma'lumotni % va litr ko'rinishida hisoblash
    percentage, liters = convert_voltage_to_percentage_and_liters(voltage)

    if 0<percentage<5:
        persi=0
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
          print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,
    elif 5<percentage<10:
        persi=5
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,
                                                             liter))                                                   
    elif 10<percentage<15:
        persi=10
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,
                                                             liter)) 
    elif 15<percentage<20:
        persi=15
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter)) 
    elif 20<percentage<25:
        persi=20
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter)) 
    elif 25<percentage<30:
        persi=25
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter))                      
    elif 30<percentage<35:
        persi=30
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter)) 
    elif 35<percentage<40:
        persi=35
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,liter))                                                           
    elif 40<percentage<45:
        persi=40
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,
                                                             liter))                                                     
    elif 45<percentage<50:
        persi=45
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,liter)) 
    elif 50<percentage<55:
        persi=50
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter)) 
    elif 55<percentage<60:
        persi=55
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter)) 
    elif 60<percentage<65:
        persi=60
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2), 
                                                                         persi, liter))
    elif 65<percentage<70:
        persi=65
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi, liter))                                                   
    elif 70<percentage<75:
        persi=70
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,liter)) 
    elif 75<percentage<80:
        persi=75
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2), persi,liter))  
    elif 80<percentage<85:
        persi=80
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2), persi,liter))  
    elif 85<percentage<90:
        persi=85
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2), persi,liter))  
    elif 90<percentage<93:
        persi=90
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2), persi,liter))  
    elif 93<percentage<95:
        persi=95
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2), persi,liter))  
    elif 95<percentage<100:
        persi=100
        liter=(450*persi)/100
         # Progress bar va litrlar chiqarish
        print('Progress: [{:<45}] {:.0f}% ({:.0f} litr)'.format('#' * int(persi / 2),
                                                             persi,liter))                                                                                                  

    # 1 sekund kutish
    time.sleep(1)

