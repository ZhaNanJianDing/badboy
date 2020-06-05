import requests
from bs4 import BeautifulSoup
def getHTML(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def getContent(url):
    html = getHTML(url)
    soup = BeautifulSoup(html,'html.parser')
    texts=soup.find_all('div',class_='content')
    return texts
def saveFile(text):
    f=open('zhananyulu.txt','w')
    for t in text:
        if len(t) > 0:
            f.writelines(t.get_text() + "\n\n")
    f.close()
def main():
    url = "https://www.diyijuzi.com/shuoshuo/19654.html"
    text = getContent(url)
    saveFile(text)
    
main()
