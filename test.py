import requests
import bs4
def get_html():
    print('enter a website url you want to crawling')
    url = input()
    response = requests.get(url)
    baidu_html = open('baidu.html','wb')
    for i in response.iter_content():
        baidu_html.write(i)

def analysis():
    example_soup = bs4.BeautifulSoup(open('baidu.html',encoding='UTF-8'),'lxml')
    elems = example_soup.select('a')
    for i in elems:
        href = i.get('href')
        print(href)
analysis()


