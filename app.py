import requests
import bs4
import webbrowser

def openurl(url):
    webbrowser.get('firefox').open_new_tab(url)


link = input('enter links: ')

a = link

res = requests.get(a)

c = res.text

soup = bs4.BeautifulSoup(res.text, 'html.parser')


html = soup

txt2 = html.get_text().split(',')

result = [i for i in txt2 if i.endswith('jpg 1280w')]

print(result)

replaceword = [s.replace(' 1280w','') for s in result]

print(replaceword)


for everylink in replaceword:
    openurl(everylink)
