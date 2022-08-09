import machine, neopixel, time
import os
import blynklib_mp
import uasyncio
from neopixel import *
from random import randint



machine.freq(160000000)

#laczenie sie z siecia
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect('WIFI NAME', 'WiFi-passwd')
        while not wlan.isconnected():
            pass
    print('Config:', wlan.ifconfig())
    
# do_connect()

#autoryzacja blynka
#BLYNK_AUTH = 'giNkyw1xFmTRkljzYjyqYzYUSdhVaLQK'
#blynk = blynklib_mp.Blynk(BLYNK_AUTH, server='192.168.0.22', port=8080,)

f = False

strip_one_led_count = 110
strip_one_led_pin = 5

strip_two_led_count = 96
strip_two_led_pin = 2


second_strip = neopixel.NeoPixel(machine.Pin(strip_two_led_pin),strip_two_led_count)
first_strip = neopixel.NeoPixel(machine.Pin(strip_one_led_pin),strip_one_led_count)
    
    
#for j in range(95,-1,-1):
    #second_strip[j] = (0,255,0)
    #second_strip.write()
    
#for x in range (0,110):
    #first_strip[x] = (255, 0, 0)
    #first_strip.write()


################################
def wheel(pos):
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

async def rainbow_cycle(wait):
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    
    for k in range (n2):
        rc_index = (i * 256 // n) + j
        npt[k] = wheel(rc_index & 255)
    npt.write()
    
    await uasyncio.sleep_ms(wait)
    if f == False:
        print("cos")
        break
#################################

        

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin,value):
    
    for x in range(95,-1,-1):
        npt[x] = (0,255,0)
        npt.write()
    
    for i in range(0,110):
        np[i] = (0,255,0)
        np.write()

            
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin,value):
    for x in range(95,-1, -1):
        npt[x] = (255,0,0)
        npt.write()
    
    for i in range(0,110):
        np[i] = (255,0,0)
        np.write()
        
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin,value):
    
    for x in range(95,-1, -1):
        npt[x] = (0,0,255)
        npt.write()
    
    for i in range(0,110):
        np[i] = (0,0,255)
        np.write()

        
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin,value):
    if (int(value[0]) == 1):
        print("Wylacz")
        
    elif (int(value[0]) == 0):
        print("Wlacz")
    
@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin,value):
    
    for j in range(95,-1,-1):
        npt[j] = (int(value[0]),int(value[1]),int(value[2]))
        npt.write()
    
    for i in range(0,110):
        np[i] = (int(value[0]),int(value[1]),int(value[2]))
        np.write()
    
@blynk.handle_event('write V6')
def write_virtual_pin_handler(pin,value):
    if (int(value[0]) == 1):
        for x in range(95,-1, -1):
            npt[x] = (255,0,255)
            npt.write()
    
        for i in range(0,110):
            np[i] = (255,0,255)
            np.write()
            
    elif (int(value[0]) == 0):
        for x in range(95,-1, -1):
            npt[x] = (0,0,0)
            npt.write()
    
        for i in range(0,110):
            np[i] = (0,0,0)
            np.write()
            
            
@blynk.handle_event('write V7')
def write_virtual_pin_handler(pin,value):
    print("kliknieto")
    if (int(value[0]) == 1):
        f = True
        uasyncio.run(rainbow_cycle(1))
    elif (int(value[0]) == 0):
        f = False