import urllib
import urllib.request

try:
    site= urllib.request.urlopen(r'http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta acessivel no momento')
else:
    print('Consegui acessar o site')
    print(site.read())