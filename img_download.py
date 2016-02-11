import requests
url = "http://cinetrooth.in/wp-content/uploads/2015/06/Madonna-Sebastian-Film-Actress-Profile-Biography-and-Upcoming-Movies.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url,headers=headers)
print(response.status_code)
if response.status_code == 200:
    f = open("Madonna/sample.jpg", 'wb')
    f.write(response.content)
    f.close()
