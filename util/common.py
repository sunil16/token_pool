import json
from datetime import datetime

FORMAT = '%Y-%m-%d %H:%M:%S.%f'

def to_string(dict_obj = None): # converting dict to json string
    return json.dumps(dict_obj)

def to_dict(dict_str = None): # converting json string to dict
    return json.loads(dict_str)

def to_dict_colletion(collection = None): # converting collection of json string to dict
    return map(lambda token: json.loads(token), collection)

def get_today_datetime():
    return datetime.now()

def to_date(date_str = None):
    return datetime.strptime(date_str, FORMAT)

def diff_with_today_times_secounds(p_date):
    if type(p_date) == str or type(p_date) == unicode:
        p_date = to_date(str(p_date))
    return (get_today_datetime() - p_date).total_seconds()
