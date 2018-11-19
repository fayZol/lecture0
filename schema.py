# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:04:05 2018

@author: octet plus


"""

import psycopg2
import sys
 

if __name__ == '__main__':
    
        con = psycopg2.connect("dbname=slurp user=postgres password=postgres")   
        cur = con.cursor()

    #    cur.execute('''CREATE TABLE Crn_Users
    #       (id INT PRIMARY KEY ,
    #       matricule text    NOT NULL,
    #       nom       text     NOT NULL,
    #       prenom    text     NOT NULL,
    #       password  text     NOT NULL );''')
    
    #    cur.execute('''CREATE TABLE Crn_Projects
    #       (id INT PRIMARY KEY ,
    #       nom text    NOT NULL,
    #       numero       integer     NOT NULL);''')
        
    #    cur.execute('''CREATE TABLE Crn_Affectation
    #       (id INT PRIMARY KEY ,
    #       id_users integer NOT NULL,
    #       id_projects integer NOT NULL);''')    
        
    
    #    cur.execute("INSERT INTO Crn_Users VALUES(1,'X124106','zerouali','faycal','lala')")
    #    cur.execute("INSERT INTO Crn_Users VALUES(2,'X124107','aerouali','gaycal','lala')")
    
    #    cur.execute("INSERT INTO Crn_Projects VALUES(1,'Paloma',0163)")
    #    cur.execute("INSERT INTO Crn_Projects VALUES(2,'Sogefilia',0067)")
    
        print("test")
        cur.execute("INSERT INTO Crn_Projects VALUES(5,'Ropstd',299)")
    #
    #    cur.execute("INSERT INTO Crn_Affectation VALUES(1,1,1)")
    #    cur.execute("INSERT INTO Crn_Affectation VALUES(2,1,2)")
        cur.execute("INSERT INTO Crn_Affectation VALUES(5,1,5)")
        
        con.commit()
        
        con.close()
    

    #    con.commit()