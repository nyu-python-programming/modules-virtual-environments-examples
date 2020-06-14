# see https://docs.python.org/3/library/urllib.html
from urllib.request import urlopen

page = urlopen("http://wikipedia.org")
# output HTTP headers
print(page.headers)

# get HTML code for page content
content = page.read() 
print(content)
