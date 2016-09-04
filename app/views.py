import nltk
import requests
from bs4 import BeautifulSoup

from flask import render_template, flash, redirect, request

from random import randint

from app import app
from app import db, models


@app.route('/', methods=['GET', 'POST'])
def index():

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
    if request.method == 'POST':
        kata_kolom_1 = isi_kolom_1[id_kolom_1-1].word
        kata_kolom_2 = isi_kolom_2[id_kolom_2-1].word
        kata_kolom_3 = isi_kolom_3[id_kolom_3-1].word
        kata_kolom_sambung = isi_kolom_sambung[id_kolom_sambung-1].word
        review = True

    return render_template('index.html',
                           kolom_1 = kata_kolom_1,
                           kolom_2 = kata_kolom_2,
                           kolom_3 = kata_kolom_3,
                           kolom_sambung = kata_kolom_sambung,
                           review=review,
                           isi_kolom_1 = isi_kolom_1,
                           isi_kolom_2 = isi_kolom_2,
                           isi_kolom_3 = isi_kolom_3,
                           isi_kolom_sambung = isi_kolom_sambung
                           )


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
