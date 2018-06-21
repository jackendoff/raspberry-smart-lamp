from flask import Flask,render_template
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
R = 10
G = 12
B = 18
pir_pin = 16
light_pin = 40
GPIO.setup(pir_pin,GPIO.IN)
GPIO.setup(light_pin,GPIO.IN)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/on')
def on():
    GPIO.setup(R,GPIO.OUT)
    GPIO.setup(G,GPIO.OUT)
    GPIO.setup(B,GPIO.OUT)

    GPIO.PWM(R,10)
    GPIO.PWM(G,10)
    GPIO.PWM(B,10)
    return render_template('main.html')
@app.route('/off')
def off():
    GPIO.setup(R,GPIO.IN)
    GPIO.setup(G,GPIO.IN)
    GPIO.setup(B,GPIO.IN)
    return render_template('main.html')
@app.route('/one')
def one():
    GPIO.setup(R,GPIO.IN)
    GPIO.setup(G,GPIO.IN)
    GPIO.setup(B,GPIO.OUT)
    
    #pwm_ledR = GPIO.PWM(R,500)
    #pwm_ledG = GPIO.PWM(G,500)
    pwm_ledB = GPIO.PWM(B,500)

    #pwm_ledR.start(100)
    #pwm_ledG.start(100)
    pwm_ledB.start(100)

    #pwm_ledR.ChangeDutyCycle(5)
    #pwm_ledG.ChangeDutyCycle(5)
    pwm_ledB.ChangeDutyCycle(1)
    return render_template('main.html')
@app.route('/two')
def two():
    GPIO.setup(R,GPIO.IN)
    GPIO.setup(G,GPIO.OUT)
    GPIO.setup(B,GPIO.IN)
    
    #pwm_ledR = GPIO.PWM(R,100)
    pwm_ledG = GPIO.PWM(G,100)
    #pwm_ledB = GPIO.PWM(B,100)n

    #pwm_ledR.start(100)
    pwm_ledG.start(100)
    #pwm_ledB.start(100)

    #pwm_ledR.ChangeDutyCycle(15)
    pwm_ledG.ChangeDutyCycle(50)
    #pwm_ledB.ChangeDutyCycle(22)
    return render_template('main.html')

@app.route('/three')
def three():
    GPIO.setup(R,GPIO.OUT)
    GPIO.setup(G,GPIO.IN)
    GPIO.setup(B,GPIO.IN)

    pwm_ledR = GPIO.PWM(R,500)
    #pwm_ledG = GPIO.PWM(G,500)
    #pwm_ledB = GPIO.PWM(B,500)

    pwm_ledR.start(100)
    #pwm_ledG.start(100)
    #pwm_ledB.start(100)

    pwm_ledR.ChangeDutyCycle(80)
    #pwm_ledG.ChangeDutyCycle(30)
    #pwm_ledB.ChangeDutyCycle(80)
    return render_template('main.html')

@app.route('/ok')
def ok():
    while True:
    #if RPi.GPIO.input(pir_pin):
        #print('jia')
        if GPIO.input(light_pin) and GPIO.input(pir_pin):
        
            GPIO.setup(R,GPIO.OUT)
            GPIO.setup(G,GPIO.OUT)
            GPIO.setup(B,GPIO.OUT)

            pwmR = GPIO.PWM(R,100)
            pwmG = GPIO.PWM(G,100)
            pwmB = GPIO.PWM(B,10)
        #pwmR.ChangeDutyCycle(100)
        #pwmG.ChangeDutyCycle(100)
        #pwmB.ChangeDutyCycle(0)
        else:
            
            GPIO.setup(R,GPIO.IN)
            GPIO.setup(G,GPIO.IN)
            GPIO.setup(B,GPIO.IN)
    
        time.sleep(0.5)
        # @app.route('/ok/exi')
        # def exi():
        #     return render_template('main.html')
    #   return render_template('main.html')
@app.route('/dance')
def dance():
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)

    pwmR = GPIO.PWM(R, 70)
    pwmG = GPIO.PWM(G, 70)
    pwmB = GPIO.PWM(B, 70)

    pwmR.start(0)
    pwmG.start(0)
    pwmB.start(0)

    try:
        t = 0.5
        while True:
            if 1 == 1:
                pwmR.ChangeDutyCycle(0)
                pwmG.ChangeDutyCycle(100)
                pwmB.ChangeDutyCycle(100)
                time.sleep(t)

                pwmR.ChangeDutyCycle(100)
                pwmG.ChangeDutyCycle(0)
                pwmB.ChangeDutyCycle(100)
                time.sleep(t)

                pwmR.ChangeDutyCycle(100)
                pwmG.ChangeDutyCycle(100)
                pwmB.ChangeDutyCycle(0)
                time.sleep(t)

                pwmR.ChangeDutyCycle(0)
                pwmG.ChangeDutyCycle(100)
                pwmB.ChangeDutyCycle(0)
                time.sleep(t)

                pwmR.ChangeDutyCycle(0)
                pwmG.ChangeDutyCycle(0)
                pwmB.ChangeDutyCycle(100)
                time.sleep(t)

                pwmR.ChangeDutyCycle(0)
                pwmG.ChangeDutyCycle(100)
                pwmB.ChangeDutyCycle(100)
                time.sleep(t)

                pwmR.ChangeDutyCycle(0)
                pwmG.ChangeDutyCycle(0)
                pwmB.ChangeDutyCycle(0)
                time.sleep(t)

                for r in range(0, 101, 20):
                    pwmR.ChangeDutyCycle(r)
                    for r in range(0, 101, 20):
                        pwmG.ChangeDutyCycle(r)
                        for r in range(0, 101, 20):
                            pwmB.ChangeDutyCycle(r)
                            time.sleep(t)

    except KeyboardInterrupt:
        pass
    pwmR.stop()
    pwmG.stop()
    pwmB.stop()

    GPIO.cleanup()


if __name__ == '__main__':
    app.run(host = '192.168.43.180')
