from django.shortcuts import render
from django.http import HttpResponse
#import mysql.connector as sql
import csv
# Create your views here.
book_id=''
book_name=''
author=''
edition=''
year=''
price=''
copies=''
def welcome(request):
    print("WELCOME")
    return render(request,'welcome.html')
"""def upload(request):
    print("student")
    if request.method=="POST":
        f=request.FILES["myfile"]
        print(f)
                  
        f1=open(f)
        data=[]
        for row in csv.reader(f):
            data.append(row)
            print(data)
            f.close()
        db=sql.connector.connect(host="127.0.0.1",user="root",password="n1k2s3s4",database="lms")
        cur=db.cursor()
        for i in data[1:]:   
            book_id=i[0]
            book_name=i[1]
            author=i[2]
            edition=i[3]
            year=i[4]
            price=i[5]
            copies=i[6]
            cur.execute("insert into book(book_id,book_name,author,edition,year,price, no_of_copies) values('"+str(book_id)+"','"+str(book_name)+"','"+str(author)+"','"+str(edition)+"','"+str(year)+"','"+str(price)+"','"+str(copies)+"')")
                
            cur.execute("commit")
        db.close()
    
    return render(request,'upload.html')
def upload_student(request):
    print("student")
    print("submit")
    f=open()
    data=[]
    for row in csv.reader(f):
        data.append(row)
        print(data)
        f.close()
        db=sql.connector.connect(host="127.0.0.1",user="root",password="n1k2s3s4",database="university")
        cur=db.cursor()
        for i in data[1:]:   
            fname=i[0]
            fid=i[1]
            faddress=i[2]
            fphoneno=i[3]
            cur.execute("insert into faculty(fname,f_id,f_address,f_phoneno) values('"+str(fname)+"','"+str(fid)+"','"+str(faddress)+"','"+str(fphoneno)+"')")
            cur.execute("commit")
            db.close()
    return render(request,'welcome.html')


def insert_student(request):
    print("student")
    return render(request,'welcome.html')




def upload_books(request):
    print("books")
    return render(request,'welcome.html')


def insert_books(request):
    print("books")
    return render(request,'welcome.html')






def upload_QP(request):
    print("QP")
    return render(request,'welcome.html')












def upload_journal(request):
    print("journal")
    return render(request,'welcome.html')
def sigaction(request):
    global name1,userid1,address1,phone1
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="nam":
               name1=value
            if key=="userid":
               userid1=value
            if key=="address":
               address1=value
            if key=="phone":
                phone1=value
        s = "insert into signup(name,userid,address,phone) VALUES (%s,%s,%s,%s)"
        val = (name1,userid1,address1,phone1)
       # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
    #return HttpResponse('signup_page.html')
    return render(request,'signup_page.html')"""





