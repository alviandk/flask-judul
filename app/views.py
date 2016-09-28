import nltk
import requests
from bs4 import BeautifulSoup

from flask import render_template, flash, redirect, request

from random import randint

from app import app
from app import db, models


@app.route('/', methods=['GET', 'POST'])
def index():

    review = False

    isi_kolom_1 = models.Kolom1.query.all()
    isi_kolom_2 = models.Kolom2.query.all()
    isi_kolom_3 = models.Kolom3.query.all()
    isi_kolom_sambung = models.KataSambung.query.all()
    
    # select kata dari database untuk masing masing kolom sesuai dengan id yang
    # didapat secara random
    judul_list=[]
    judul_dict = {'judul': [], 'hits': [], 'kolom_2': [], 'hits_google': []}
    if request.method == 'POST':
        review = True
        for i in range(10):
            judul_list.append(random_judul())
        #judul_list.sort(reverse=True)
        judul_list = sorted(judul_list, key=lambda k: k['hits'], reverse=True) 

        print(judul_list)
        for judul in judul_list:
            judul_dict['judul'].append(judul['judul'])
            judul_dict['hits'].append(judul['hits'])
            judul_dict['hits_google'].append(judul['hits_google'])
            judul_dict['kolom_2'].append(judul['kolom_2'])
    
    return render_template('index.html',
                           review=review,
                           isi_kolom_1 = isi_kolom_1,
                           isi_kolom_2 = isi_kolom_2,
                           isi_kolom_3 = isi_kolom_3,
                           isi_kolom_sambung = isi_kolom_sambung,
                           juduls=judul_dict
                           )


def random_judul():

    kata_kolom_1 = ''
    kata_kolom_2 = ''
    kata_kolom_3 = ''
    kata_kolom_sambung = ''
    review = False

    isi_kolom_1 = models.Kolom1.query.all()
    isi_kolom_2 = models.Kolom2.query.all()
    isi_kolom_3 = models.Kolom3.query.all()
    isi_kolom_sambung = models.KataSambung.query.all()


    # mendapatkan banyaknya isi kolom
    panjang_kolom_1 = len(models.Kolom1.query.all())
    panjang_kolom_2 = len(models.Kolom2.query.all())
    panjang_kolom_3 = len(models.Kolom3.query.all())
    panjang_kolom_sambung = len(models.KataSambung.query.all())

    # mendapatkan id secara raandom untuk masing2 kolom
    id_kolom_1 = randint(1, panjang_kolom_1)
    id_kolom_2 = randint(1, panjang_kolom_2)
    id_kolom_3 = randint(1, panjang_kolom_3)
    id_kolom_sambung = randint(1, panjang_kolom_sambung)

    # select kata dari database untuk masing masing kolom sesuai dengan id yang
    # didapat secara random
    kata_kolom_1 = isi_kolom_1[id_kolom_1-1].word
    kata_kolom_2 = isi_kolom_2[id_kolom_2-1].word
    kata_kolom_3 = isi_kolom_3[id_kolom_3-1].word
    kata_kolom_sambung = isi_kolom_sambung[id_kolom_sambung-1].word

    s = requests.session()
    s.headers = {
                    'Host': 'library.gunadarma.ac.id',
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Referer': 'http://library.gunadarma.ac.id/epaper',
                    'Cookie': '__utma=9989098.1557719901.1463302466.1463302466.1463302466.1; __utmz=9989098.1463302466.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=93494912.1777379700.1467768547.1467768547.1467855432.2; __utmz=93494912.1467768547.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); prefs_navclick=0; prefs_accordion=0; prefs_search=0; prefs_masthead=0; prefs_photo=0; prefs_background=0; PHPSESSID=0c8afa87f951278226ec170e4b5ead51; __utmb=93494912.3.9.1467855435026; __utmc=93494912; __utmt=1',
                    'Connection': 'keep-alive'
                }

    print('Login to epaper gunadarma')
    username = 'mridwan_adip'
    password = '1994-03-27'
    url = 'http://library.gunadarma.ac.id/epaper/login/'
    r = s.post(url, data={'username': username, 'password': password, 'login': 'yes','login.x': 79, 'login.y': 27})
    print(r.url)
    s.headers={
                'Host': 'library.gunadarma.ac.id',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://library.gunadarma.ac.id/epaper.advanced',
                'Cookie': '__utma=9989098.1557719901.1463302466.1463302466.1463302466.1; __utmz=9989098.1463302466.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=93494912.1777379700.1467768547.1467768547.1467855432.2; __utmz=93494912.1467768547.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); prefs_navclick=0; prefs_accordion=0; prefs_search=0; prefs_masthead=0; prefs_photo=0; prefs_background=0; PHPSESSID=0c8afa87f951278226ec170e4b5ead51; __utmb=93494912.3.9.1467855435026; __utmc=93494912',
                'Connection': 'keep-alive'
              }

    
    url = 'http://library.gunadarma.ac.id/epaper/search/?q={}&judul=&nama=&pembimbing='.format(kata_kolom_2)
    r=s.get(url)
    content = BeautifulSoup(r.content)
    
    hits = content.find('h4', {'class': 'alert-heading'})
    print(hits, 'hits')
    if hits:
        hits= hits.text.replace('Result! Found ', '')
        hits= hits.replace(' ePaper on database ', '')
    else:
        hits=0


    url = 'https://scholar.google.com/scholar?q={}%20{}%20{}%20{}'.format(kata_kolom_1, kata_kolom_2, kata_kolom_3, kata_kolom_sambung )
    r=requests.get(url)
    content = BeautifulSoup(r.content)
    print(content, 'content')
    hits_google = content.find('div', {'id': 'gs_ab_md'})
    print(hits_google, '1')
    if hits_google:
        hits_google = hits_google.text.split(' ')
        hits_google = hits_google[1]
        hits_google = hits_google.replace(',', '')
    else:
        hits_google=0

    return {'judul': '{} {} {} {}'.format(kata_kolom_1, kata_kolom_2, kata_kolom_sambung, kata_kolom_3), 
            'hits': int(hits), 'kolom_2': kata_kolom_2, 'hits_google': int(hits_google),}



@app.route('/update-kolom-2', methods=['GET'])
def update_kolom_2():

    
    s = requests.session()
    url = 'http://spectrum.ieee.org/computing/'
    r = s.get(url)
    content = BeautifulSoup(r.content)
    titles = content.findAll('h3', {'class': 'article-title'})
    for title in titles:
        tokens = nltk.word_tokenize(title.text)
        tagged = nltk.pos_tag(tokens)
        for word, pos in tagged:
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                
                kolom_2 = models.Kolom2.query.filter_by(word=word).first()
                if not kolom_2:
                    w = models.Kolom2(word=word)
                    db.session.add(w)
                    db.session.commit()

    return redirect('/')


@app.route('/update-kolom-3', methods=['GET'])
def update_kolom_3():

    
    s = requests.session()
    url = 'http://www.informationweek.com/whitepaper/'
    r = s.get(url)
    content = BeautifulSoup(r.content)
    titles = content.find('select', {'id': 'body-topics-search'}).findAll('option')
    for title in titles:
        kolom_3 = models.Kolom3.query.filter_by(word=title.text).first()
        if not kolom_3:
            w = models.Kolom3(word=title.text)
            db.session.add(w)
            db.session.commit()

    return redirect('/')
