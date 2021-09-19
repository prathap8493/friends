#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:55:07 2021

@author: student
"""
from flask import Flask,render_template,url_for,request,redirect
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("total.html")
@app.route("/home.html")
def ho():
        return render_template("home.html")
@app.route("/about.html")
def ab():
        return render_template("about.html")
@app.route("/form.html")
def login():
        return render_template("form.html")
database={'prathap':'prathap123','ajay':'ajay123','taja':'teja123','zaheer':'zaheer123','sreekanth':'sreekanth123','upendra':'upendra123'}
@app.route("/display",methods=['POST','GET'])
def sign():
    #if request.form=="post":
         name=request.form["name"]
         password=request.form["password"]
         gender=request.form["radio"]
         email=request.form["email"]
         if name not in database:
             return render_template("form.html",info="invalid user")
         else:
             if database[name]!=password:
                 return render_template("form.html",info="invalid password")
             else:
                 return redirect(url_for('submit',name_1=name,gender_1=gender,email_1=email))
@app.route("/submit/<name_1><gender_1><email_1>")
def submit(name_1,gender_1,email_1):
   return render_template("result.html",name1=name_1,gender1=gender_1,email1=email_1)
            
if __name__=="__main__":
    app.run(debug=True)