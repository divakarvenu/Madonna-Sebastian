import requests
from bs4 import BeautifulSoup

#adding headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#change your keyword after q assignment in case of space add +
r = requests.get('https://www.google.co.in/search?safe=off&site=&tbm=isch&source=hp&biw=1366&bih=657&q=madonna+sebastian',headers=headers)
soup = BeautifulSoup(r.content,"html.parser")
#intiallising counter
i=0
for div in soup.findAll("a", { "class" : "rg_l" }):
        #incrementing it to count images
        i=i+1      
        #retriving first small box images
        img=requests.get('https://www.google.co.in'+div['href'],headers=headers)
        inner_soup = BeautifulSoup(img.content,"html.parser")
        og_image = inner_soup.find('meta', attrs={'property': 'og:image'})
        #retriving image urls
        url = og_image['content']
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            f = open("Madonna/"+str(i)+".jpg", 'wb')
            f.write(response.content)
            f.close()

print("Total No of images found"+str(i));
        
        


