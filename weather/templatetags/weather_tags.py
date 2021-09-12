import json
from datetime import datetime
from django import template
from pytz import timezone as tz, utc
from dateutil import parser

register = template.Library()


@register.filter
def icon(forecast):
    f = open('data.json')
    data = json.load(f)
    f.close()
    return data[forecast['pod']][str(forecast['weather']['code'])]


@register.simple_tag
def tz_time(timezone):
    TZ = tz(timezone)
    date = datetime.now(TZ)
    return date.strftime('%H:%M')


@register.filter
def get_tz_time(date, timezone):
    dateTime = parser.parse(date)
    print(dateTime)
    dateTime = dateTime.replace(tzinfo=utc)
    timeZone = tz(timezone)
    tz_time = dateTime.astimezone(timeZone)
    print(tz_time)
    return tz_time.strftime('%H:%M')
