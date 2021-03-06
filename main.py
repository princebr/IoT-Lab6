#!/usr/bin/python
import time
from sense import PiSenseHat
from flask import *

# Create Pi SenseHat object
pi_sense_hat = PiSenseHat()

# ---------------- FUNCTIONS ------------------
def get_sensor_values():
    return pi_sense_hat.getAllSensors()


# ---------------- API ROUTES -----------------
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# ------------ ENDPOINT: /myData --------------
# curl http://10.0.1.41/myData
# ---------------------------------------------
@app.route('/myData')
def myData():
    def get_values():
        while True:
            data_obj = get_sensor_values()
            yield('data: {0}\n\n'.format(data_obj))
            time.sleep(1.0)
    return Response(get_values(), mimetype='text/event-stream')



if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
