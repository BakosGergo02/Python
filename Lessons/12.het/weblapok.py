import urllib.request

import requests

def get_page(link):
    response = urllib.request.urlopen(link)
    raw = response.read()
    text = raw.decode('utf-8')
    return text

def get_webstite_object(link,dest):
    urllib.request.urlretrieve(link,dest)

def main():
    #get_page('https://www.python.org/')

    #url = 'https://www.http.cat/403'
    #dest = "C:/Users/Dell/PycharmProjects/Szkriptnyelvek\.venv\12.het\403.png"

    #get_webstite_object(url,dest)

    url = "https://suvicsabika.github.io/"
    source = requests.get(url)



    cel = source.sp
    print(cel)



if __name__ == '__main__':
    main()