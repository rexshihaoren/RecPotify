import subprocess
subprocess.call("sh ./run-redis.sh &", shell=True)
subprocess.call("sh ./run-celery.sh &", shell=True)
import os
from app import app
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
