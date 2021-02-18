import LED_control
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

LED_control.start()


@app.route('/0')
def off():
    LED_control.led_off()
    return 'LED OFF'


@app.route('/1')
def on():
    LED_control.led_on()
    return 'LED ON'


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5005)

LED_control.ende()

print('DONE')
