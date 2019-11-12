from flask import Flask
from pool_service import cache_pool_setting
from flask_apscheduler import APScheduler

app = Flask(__name__)
app.config.from_pyfile('./config.py')
pool_service_instance = cache_pool_setting.init_token_pool(app)

class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'app:pool_service_instance.is_token_expired',
            'args': (),
            'trigger': 'interval',
            'seconds': int(app.config['WAIT_TIME_SECONDS'])
        }
    ]
    
@app.route('/get_token', methods = ['GET','POST'])
def get_token():
    token = pool_service_instance.get_available_token()
    return { "token" : token }

@app.route('/get_stats', methods = ['GET','POST'])
def get_stats():
    stats = pool_service_instance.get_stats()
    return { "token_stats" : stats }

if __name__ == '__main__':
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug = True)
