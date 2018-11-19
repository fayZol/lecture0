# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:50:04 2018

@author: octet plus
"""

from flask import Flask, render_template, request
import FirstPostGresDb as Crs
import random



app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/projets",methods=["GET", "POST"])
def projets():
    matricule = request.form.get("matricule")
    matricule = 'X124106'
    password = 'lala'
    #password = request.form.get("password")
    row = Crs.req(matricule,password)
    
    if row:
        strAnswer = "Coucou " + str(row[2])
        strAnswer = strAnswer + "\n Projets   Num"
        idUser = row[0]
        rows = Crs.listOfProjects(idUser)
        palette = []
        for ro in rows:
            colorHex =  "#{:06x}".format(random.randint(0, 0xFFFFFF))
            strAnswer = strAnswer + "\n" + str(ro[1]) + '   ' + str(ro[2])
            #palette.add(colorHex)
            
            liz = list(ro)
            liz.append(colorHex)
            palette.append(colorHex)
            ro = tuple(liz)
            
        print(rows)
        
        
        return render_template("index.html", rows=rows, colorHex = colorHex, palette = palette)

#@app.route('/my-link/')
#def my_link():
#    data = MyData()
#    return data

if __name__ == '__main__':

    #app.run(host= '0.0.0.0')
    app.run(debug = True)
    
    
    
    
    #def shutdown_server():
#    func = request.environ.get('werkzeug.server.shutdown')
#    if func is None:
#        raise RuntimeError('Not running with the Werkzeug Server')
#    func()
#
#@app.route('/shutdown', methods=['POST'])
#def shutdown():
#    shutdown_server()
#    return 'Server shutting down...'