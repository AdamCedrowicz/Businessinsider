# importy
from bs4 import BeautifulSoup
import requests
lst = list(range(1,30+1))
section = 'https://businessinsider.com.pl/twoje-pieniadze'
# wybieramy sekcje z której bierzemy artykuł
for v in lst:
    # Tworzymy listę linków z całej sekcji
    page = section+'?page='+str(v)
    result = requests.get(page)
    soup = BeautifulSoup(result.text , "html.parser")
    # zbieramy wszystkie darmowe artykuły ze strony
    links = []
    for link in soup.findAll('a'):
        if section in link.get('href') and "subskrypcja?" not in link.get('href') :
            links.append(link.get('href'))
    for i in links:
        # !!! pojedynczy artykuł do pliku
        url = i
        result = requests.get(url)
        soup = BeautifulSoup(result.text , "html.parser")
        cancellled_characters = ['/',':','*','?','"','<','>','|']
        # wyciagamy tytuł
        title = soup.find('h1', {'class' : 'article_title'}).get_text()
        title = ''.join([c for c in title if c not in cancellled_characters])
        # wybieramy czesci tekstu i łączymy je w jeden
        rows = soup.find_all('p', {'class' : 'article_p'})
        content_parts = []
        for row in rows:         
            content_parts.append(row.get_text())
        content = ' '.join(content_parts)
        # zapisujemy do pliku
        with open(title + '.txt', 'w') as f:
            f.write(content)
        # czyszczenie zmiennych
        content_parts.clear() 
        content = None