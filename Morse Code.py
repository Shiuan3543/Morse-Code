import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
led = 18
GPIO.setup(led,GPIO.OUT)

Code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        
        '?': '..--..', '/': '-..-.',  '(': '-.--.-',
        '_': '-.--.-', '-': '-....-', '.': '.-.-.-'
        }

def short():
    GPIO.output(led,True)
    sleep(0.1)
    GPIO.output(led,False)
    sleep(0.5)
def long():
    GPIO.output(led,True)
    sleep(0.5)
    GPIO.output(led,False)
    sleep(0.5)
    
def change(i):
    temp = Code[i]
    for j in temp:
        if(j=='-'):
            long()
        else:
            short()
    sleep(1)
                
while True:
    target = (input("Please Enter Some Wrods: ")).upper()
    a = target.split()
    for i in a:
        for k in i:
            change(k)
        
    
    


    
    
