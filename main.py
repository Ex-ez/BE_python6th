import urllib.request

url = 'https://www.google.com'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

html = response.read()

print(html)