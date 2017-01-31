# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request, parse

def fetch_xml(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
    return data

class WeatherSaxHandler(object):
    def __init__(self):
        self.result = dict()
        self.count = 0
        self.result['forecast'] = dict()

    def start_element(self,name,attrs):
        if name == 'yweather:location':
            self.result['location'] = attrs
        if name == 'yweather:forecast':
            self.count += 1
            if self.count <= 2:
                self.result['forecast'][str(self.count)] = attrs
                

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    rl = handler.result['location']
    rw = handler.result['forecast']
    weather = dict()
    weather['city'] = rl.pop('city')
    weather['country'] = rl.pop('country')
    weather['today'] = rw['1']
    weather['tomorrow'] = rw['2']
    return weather

# 测试:
data = fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330')
weather = parse_weather(data)
print('Weather:', str(weather))
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == '20', weather['today']['low']
assert weather['today']['high'] == '33', weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == '21', weather['tomorrow']['low']
assert weather['tomorrow']['high'] == '34', weather['tomorrow']['high']