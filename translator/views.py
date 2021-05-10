from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def translate(request):
    if request.method == 'POST':
        data = request.POST
        word = data['world']
        load = {'q':word}
        r = requests.get('https://www.englishnepalidictionary.com/',params=load).text
        soup = bs(r,'lxml')
        meaning = soup.find('div',class_="search-result").h3.text
        context = {
            'meaning':meaning
        }
        return render(request,'templates/index.html',context)
    return render(request,'templates/index.html')