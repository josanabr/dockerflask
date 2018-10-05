from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Gutten morgen"

@app.route('/loadavg')
def load_avg():
   output = subprocess.check_output(['cat','/proc/loadavg'])
   return output[:-1]

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
