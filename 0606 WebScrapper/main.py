from django.shortcuts import redirect
from flask import Flask, render_template, request
from jobscrapper import indeed_get_job

app = Flask("Scrapper")

db = {}     # fakeDB

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower() # 사용자 입력 초기화해주기
        fromDb = db.get(word)

        if fromDb:  # 이전에 검색한 기록이 있다면? db에 저장되어 있다면, 그걸 보여주자
            jobs = fromDb
        else:       # 없다면 검색해서 db에도 넣어주자
            jobs = indeed_get_job(word)    
            db[word] = jobs

    else:       # 아무것도 입력하지 않은 경우 home.html으로 다시 연결해주기
        return redirect('/')
    return render_template(
        "report.html", 
        word=word, 
        resultNum=len(jobs),
        jobs=jobs)

app.run(host="0.0.0.0")