# OST45050C1A-Wドライバー(RP2040)

import array
from machine import Pin
import rp2
import time

# 接続しているLEDの数
LEDS = 5

# 信号を出力するGPIOピン番号
PIN_NUMBER = 22

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=32)
def driver():
    T1 = 2
    T2 = 3
    T3 = 5
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine with the driver program, outputting on Pin(PIN_NUMBER).
sm = rp2.StateMachine(0, driver, freq=8_000_000, sideset_base=Pin(PIN_NUMBER))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(LEDS)])



# Example


# clour set : (r, g, b, w, lum) | [r, g, b, w => 0~255],[lum (輝度:デフォルト100%) => 0~100]
def colour_set(r=0, g=0, b=0, w=0, lum=100):
    return g * lum // 100 * 16777216 + r * lum // 100 * 65536 + b * lum // 100 * 256 + w * lum // 100


red        =  (255, 0, 0, 0)
green      =  (0, 255, 0, 0)
blue       =  (0, 0, 255, 0)
cyan       =  (0, 255, 255, 0)
magenta    =  (255, 0, 255, 0)
yellow     =  (255, 255, 0, 0)
white_rgb  =  (255, 255, 255 , 0)
white      =  (0, 0, 0, 255)

colours = [red, green, blue, cyan, magenta, yellow, white_rgb, white]


def wave_colours():

    while True:

        for colour in colours:

            for brightness in range(0, 181, 20):
                if brightness > 100:
                    brightness = 100

                for n in range(4, -1, -1):
                    ar[n] = ar[n-1]
                    if n == 0:
                        ar[n] = colour_set(*colour + (brightness,))

                sm.put(ar, 0)
                time.sleep_ms(50)

            for brightness in range(180, -1, -20):
                if brightness > 100:
                    brightness = 100

                for n in range(4, -1, -1):
                    ar[n] = ar[n-1]
                    if n == 0:
                        ar[n] = colour_set(*colour + (brightness,))

                sm.put(ar, 0)
                time.sleep_ms(50)


wave_colours()
