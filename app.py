from flask import Flask,jsonify,request
import csv

app=Flask(__name__)

all_articles=[]

with open("articles.csv",encoding='UTF-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
not_liked_articles=[]

@app.route("/get_articles",methods=['GET'])
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/like_article",methods=['POST'])
def like_article():
    article=all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unlike_article",methods=['POST'])
def unlike_article():
    article=all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201


if __name__=="__main__":
    app.run()
