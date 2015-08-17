#!/bin/env python
__author__ = 'mjob'

try:
	# For Python 3.0 and later
	from urllib.request import urlopen
except ImportError:
	# Fall back to Python 2's urllib2
	from urllib2 import urlopen
import json, locale, os.path as path, subprocess, os
from datetime import datetime, timedelta

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

with open('.apikey', 'r') as f:
	apiKey = f.readline()

url = 'https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=ok-lab-chemnitz&status=upcoming&page=1&sign=true&key=' + apiKey

result = urlopen(url, timeout=10)

if result.code != 200:
	print('HTTP status is not 200')
	raise SystemExit()

data = json.loads(result.read().decode('utf-8'))
event = data['results'][0]

timestamp = event['time']/1000

date = datetime.fromtimestamp(timestamp)

timeString = date.strftime('%H:%M') + ' - '

if event['duration']:
	end = date + timedelta(milliseconds=event['duration'])
	timeString += end.strftime('%H:%M')
else:
	timeString += 'open end'

venue = ', '.join([event['venue']['name'], event['venue']['address_1'], event['venue']['city']])

with open(path.join('_data', 'treffen.template')) as f:
	template = f.read()
	template = template.replace('{{WEEKDAY}}', date.strftime('%A'))
	template = template.replace('{{DAY}}', date.strftime('%d'))
	template = template.replace('{{MONTH}}', date.strftime('%B %Y'))
	template = template.replace('{{TIME}}', '"' + timeString + '"')
	if event['venue']['name'] != 'ChaosTreff Chemnitz':
		template = template.replace('{{LOCATION}}', 'location: ' + venue)
	else:
		template = template.replace('{{LOCATION}}', '#')
	with open(path.join('_data', 'treffen.yml'), 'w+') as fw:
		fw.write(template)

os.chdir('_data')
p = subprocess.Popen(['git', 'status', '--short'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()

if stdout and 'treffen.yml' in str(stdout):
	subprocess.call(['git', 'add', 'treffen.yml'])
	subprocess.call(['git', 'commit', '--quiet', '-m', '"event updated"'])
	#subprocess.call(['git', 'push', '--quiet'])
	print('I pushed that shit!')
