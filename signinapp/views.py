from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
import mysql.connector as sql
from decimal import Decimal

em=''
pwd=''
# Create your views here.
def signaction(request):
    if request.method == "POST":
    
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        
        
        try:
            conn = sql.connect(host="localhost", user="root", passwd="123456789", database="registre")
            cursor = conn.cursor()

    
            query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            data = (first_name, last_name, email, password)
            cursor.execute(query, data)

        
            conn.commit()

            
            cursor.close()
            conn.close()
        except Exception as e:
        
            print("Error:", e)
            return render(request, 'error.html')

    return render(request, 'registre.html')


def storeaction(request):
    if request.method == "POST":
       
    
        nom = request.POST.get('nom','')
        description = request.POST.get('description' , '')
        prix = request.POST.get('prix' , '')
        stock = request.POST.get('stock', '')
       
        
        
        
        try:
            conn = sql.connect(host="localhost", user="root", passwd="123456789", database="registre")
            cursor = conn.cursor()

    
            query = "INSERT INTO signinapp_article (nom, description, prix, stock) VALUES (%s,%s, %s, %s)"
            data = (nom, description, prix, stock)
            cursor.execute(query, data)

        
            conn.commit()

            
            cursor.close()
            conn.close()
        except Exception as e:
        
            print("Error:", e)
            return render(request, 'error1.html')

    return render(request, 'produit.html')



def logaction(request):
    global em, pwd
    
    if request.method == "POST":
        # Establishing connection to the MySQL database
        m = sql.connect(host="localhost", user="root", passwd="123456789", database="registre")
        cursor = m.cursor()
        
        # Retrieving data from POST request
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        
        # Executing SELECT query to check for user
        c = "SELECT * FROM user WHERE email = %s AND password = %s"
        cursor.execute(c, (em, pwd))
        
        # Fetching results
        rows = cursor.fetchall()
        
        # Checking if any row matches the provided credentials
        if not rows:
            return render(request, 'error.html')
        else:
            return render(request, 'welcome.html')

    return render(request, 'sign_in.html')