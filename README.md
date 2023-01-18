# OST45050C1A-W-driver for Raspberry Pi Pico (RP2040)

MicroPython用のドライバーが見つからなかったため、[Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)の3.9.2. WS2812 LED (NeoPixel)を参考に作ったものです。


接続するLEDの数を'LEDS'に、信号線を接続するGPIOピン番号を'PIN_NUMBER'に、それぞれ代入してください。

Exampleコードでは「赤、緑、青、シアン、マゼンタ、イエロー、赤・緑・青全点灯の白、白」の色が順番に流れるように点灯します。
