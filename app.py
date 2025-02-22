from flask import Flask
import subprocess
import getpass
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Amit"
    system_username = getpass.getuser()
    india_tz = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(india_tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    return f"""
    <h3>Name: {full_name}</h3>
    <h3>Username: {system_username}</h3>
    <h3>Server Time (IST): {now_ist}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
