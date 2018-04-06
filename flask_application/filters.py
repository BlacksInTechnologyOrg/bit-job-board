import datetime
import math

from flask_application import app


@app.template_filter('time_ago')
def time_ago(value):
    delta = datetime.datetime.now() - value
    if delta.days == 0:
        formatting = 'today'
    elif delta.days < 10:
        formatting = '{0} days ago'.format(delta.days)
    elif delta.days < 28:
        formatting = '{0} weeks ago'.format(int(math.ceil(delta.days/7.0)))
    elif value.year == datetime.datetime.now().year:
        formatting = 'on %d %b'
    else:
        formatting = 'on %d %b %Y'
    return value.strftime(formatting)

@app.template_filter('datetimeformat')
def datetimeformat(value):
    print(value)
    newdate = datetime.datetime.fromtimestamp(value/1000).strftime('%Y-%m-%d')
    print(newdate)
    return newdate