from django.shortcuts import render,redirect
 
from django.http import HttpResponse
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="mysql_db", user="root", passwd="4444", database='Base_Ejemplo')
print('Successfully connected to database')
cur = conn.cursor()

def home(request):
    return  render(request,'home.html')


def list_jugadores(request):
    cur.execute("SELECT * FROM jugadores")
    data = cur.fetchall()
    return render(request, 'view.html', {'categories': data})   


def jugador_create(request):
    return render(request, 'add.html')   


def add_jugador(request):
    if request.method == 'POST':
        name = request.POST['txt1']
        dorsal = request.POST['dor1']
        cur.execute("INSERT INTO jugadores(nombre, dorsal) VALUES ('{}',{})".format(name,dorsal))
        conn.commit()
        return redirect(jugador_create) 
    else:
        return redirect(jugador_create)


def delete_jugador(request,id):
    cur.execute("delete from jugadores where id_jugador = {}".format(id))
    conn.commit()
    return redirect(list_jugadores) 


def edit_jugador(request,id):
    cur.execute("select * from jugadores where id_jugador = {}".format(id))
    data = cur.fetchone()
    print(list(data))
    return render(request, 'edit.html', {'categories': data})   


def update_jugador(request):
    if request.method == 'POST':
        print(request.POST)
        idjugador = request.POST['txt1']
        new_name = request.POST['txt2']
        new_dorsal = request.POST['dor2']
        cur.execute("update jugadores set nombre ='{}', dorsal = {} where id_jugador ='{}'".format(new_name,new_dorsal,idjugador))
        conn.commit()
        return redirect(list_jugadores) 
    else:
        return redirect(list_jugadores)