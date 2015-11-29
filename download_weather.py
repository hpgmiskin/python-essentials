import urllib.request

url="http://weather.noaa.gov/pub/data/observations/metar/decoded/EGLL.TXT"
weather_data = urllib.request.urlopen(url).read()
print(weather_data)

# Challenge
# Find the current weather in london

# Useful functions
demo = 'name: number'
demoList = demo.split(':')
print(demoList)

# Lines
demo = '''
line 1
line 2
'''
demoList = demo.split('\n')
print(demoList)