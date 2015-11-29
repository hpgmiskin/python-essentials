import urllib.request

url="http://weather.noaa.gov/pub/data/observations/metar/decoded/EGLL.TXT"
weatherData = urllib.request.urlopen(url).read().decode('utf-8')

# Waeather data
for line in weatherData.split('\n'):
    print(line)

# Challenge
# ======================================================================
# Find the current weather in london






# Useful functions
# ======================================================================
demo = 'name: number'
demoList = demo.split(':')
print(demoList)