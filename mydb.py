import mysql.connector

database=mysql.connector.connect(host='localhost',user='root',passwd='')

# prepare cursor object 
cursorobject=database.cursor()

#create database 
cursorobject.execute("CREATE DATABASE CRM")

print("first time connection mysql")
