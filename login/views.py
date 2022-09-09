import os
from django.shortcuts import render
from io import TextIOWrapper
from django.http import HttpResponse
import mysql.connector as sql
import datetime
import csv
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def question(request):
    return render(request,'question_paper.html')
def bscience(request):
    return render(request,'basic_science.html')
def comis(request):
    return render(request,'com_is.html')
def mechanical(request):
    return render(request,'mech.html')
def maths(request):
    return render(request,'maths.html')
def civil(request):
    return render(request,'civil.html')
def ec(request):
    return render(request,'ec.html')
def table(request):
    return render(request,'table.html')
def fadmin(request):
    return render(request,'fadmin.html')
def firstadminpg(request):
    return render(request,'firstadminpg.html')
def adminm(request):
    return render(request,'adminm.html')

def deletebook(request):
    return render(request,'deletebook.html')
def UpdBook(request):
    return render(request,'UpdBook.html')
def Supload(request):
    return render(request,'Supload.html')
def Sregister(request):
    return render(request,'Sregister.html')
def Stlist(request):
    return render(request,'Stlist.html')
def insertbook(request):
    return render(request,'insertbook.html')
def semCI3(request):
    return render(request,'3semCI.html')
def semCI4(request):
    return render(request,'4semCI.html')
def semCI5(request):
    return render(request,'5semCI.html')
def semCI6(request):
    return render(request,'6semCI.html')
def semCI7(request):
    return render(request,'7semCI.html')
def semCI8(request):
    return render(request,'8semCI.html')
def semCIV3(request):
    return render(request,'3semCIV.html')
def semCIV4(request):
    return render(request,'4semCIV.html')
def semCIV5(request):
    return render(request,'5semCIV.html')
def semCIV6(request):
    return render(request,'6semCIV.html')
def semCIV7(request):
    return render(request,'7semCIV.html')
def semCIV8(request):
    return render(request,'8semCIV.html')
def semME3(request):
    return render(request,'3semME.html')
def semME4(request):
    return render(request,'4semME.html')
def semME5(request):
    return render(request,'5semME.html')
def semME6(request):
    return render(request,'6semME.html')
def semME7(request):
    return render(request,'7semME.html')
def semME8(request):
    return render(request,'8semME.html')
def semECE3(request):
    return render(request,'3semECE.html')
def semECE4(request):
    return render(request,'4semECE.html')
def semECE5(request):
    return render(request,'5semECE.html')
def semECE6(request):
    return render(request,'6semECE.html')
def semECE7(request):
    return render(request,'7semECE.html')
def semECE8(request):
    return render(request,'8semECE.html')


def ad_logaction(request):
    global em,pwd
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        
        if em=='aitlib@gmail.com' and pwd=='123':
            return render(request,"adminm.html")
        else:
            return render(request,"error.html")

    return render(request,'admin_login.html')
def insertbook(request):
    global book_name,book_id,author,price,no_of_copies,publication,edition,sem1,year,branch
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="bn":
               book_name=value
            if key=="bi":
               book_id=value
            if key=="an":
               author=value
            if key=="pri":
                price=value
            if key=="noc":
               no_of_copies=value
            if key=="pn":
               publication=value
            if key=="ed":
               edition=value
            if key=="sem1":
               sem1=value
            if key=="year":
               year=value
            if key=="dept":
               branch=value
        s = "insert into book(book_id,book_name,author,price,no_of_copies,publication,edition,sem1,year,branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (book_id,book_name,author,price,no_of_copies,publication,edition,sem1,year,branch)
       # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
        m.close()
    return render(request,'insertbook.html')
def Sregister(request):
    global usn,name,card_no,email,phone_no,sem,department,year,address
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="usn":
               usn=value
            if key=="nm":
               name=value
            if key=="cn":
               card_no=value
            if key=="em":
                email=value
            if key=="pn":
               phone_no=value
            if key=="ad":
               address=value
            if key=="sem":
               sem=value
            if key=="year":
               year=value
            if key=="dept":
               department=value
        s = "insert into student(usn,name,card_no,email,phone_no,sem,department,year,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (usn,name,card_no,email,phone_no,sem,department,year,address)
         # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
        m.close()
    return render(request,'Sregister.html')


def firstadminpg(request):
    print('hello')
    global sname,sid,checkin,checkout,sem1,year,branch
    print(request.method)
    if request.method=="POST":
        
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="sn":
               sname=value
            if key=="usn":
               sid=value
            if key=="chin":
               checkin=value
            if key=="chout":
                checkout=value
            
            if key=="sem":
               sem1=value
            if key=="year":
               year=value
            if key=="dept":
               branch=value
        s = "insert into log_book(sname,usn,checkin,checkout,sem,year,branch) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (sname,sid,checkin,checkout,sem1,year,branch)
       # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
        m.close()
    return render(request,'firstadminpg.html')


def logbook(request):
    context={}
    b=["sname","usn","cin","cout","sem","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    c="select * from log_book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))


    m.close()
    return render(request,'checkin.html',{"data":context})


    return render(request,'firstadminpg.html')


def display_book(request):
    print("display")
    context={}
    b=["book_id","book_name","author","price","no_of_copies","publication","edition","sem1","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    
    c="select book_id,book_name,sem1,branch,no_of_copies,publication,edition from book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    m.close()
    return render(request,"table.html", {"data":context})
def display_book1(request):
    print("display")
    context={}
    b=["book_id","book_name","author","price","no_of_copies","publication","edition","sem1","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    
    c="select book_id,book_name,sem1,branch,no_of_copies,publication,edition from book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    m.close()
    return render(request,"displayLib.html", {"data":context})


"""def displaybook(request):
    print("display")
    context={}
    b=["book_id","book_name","author","price","no_of_copies","publication","edition","sem1","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    
    c="select book_id,book_name,sem1,branch,no_of_copies,publication,edition from book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    m.close()
    return render(request,"displaylib2.html", {"data":context})"""



def student_page(request):
    print("display")
    context={}
    b=["book_id","book_name","author","price","no_of_copies","publication","edition","sem1","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    
    c="select book_id,book_name,sem1,branch,no_of_copies,publication,edition from book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    m.close()
    return render(request,"displayLib.html", {"data":context})

def Stlist(request):
    context={}
    b=["sname","sid","address","email","phone","cardno","sem","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    c="select *from student"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    m.close()
    return render(request,'Stlist.html',{"data":context})


def student_logaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="usn":
                pwd=value
        
        c="select * from student where email='{}' and usn='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())

        if t==(em=='email' and pwd=='usn'):
            return render(request,"displayLib.html")
        else:
            return render(request,'error.html')
        
        """if t==():
            return render(request,'error.html')
        else:
            return render(request,"displayLib.html")"""
        m.close()
    return render(request,'student_login.html')

def UpdBook(request):
    global book_name,book_id,author,price,no_of_copies,publication,edition,sem1,year,branch
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="bn":
               book_name=value
            if key=="bid":
               book_id=value
            if key=="an":
               author=value
            if key=="pc":
                price=value
            if key=="nc":
               no_of_copies=value
            if key=="pn":
               publication=value
            if key=="ed":
               edition=value
            if key=="sem":
               sem1=value
            if key=="year":
               year=value
            if key=="dept":
               branch=value
        s = "update book set book_name=%s,author=%s,price=%s,no_of_copies=%s,publication=%s,edition=%s,sem1=%s,year=%s,BRANCH=%s where book_id=%s"
        val = (book_name,author,price,no_of_copies,publication,edition,sem1,year,branch,book_id)
        # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
        m.close()
    return render(request,'UpdBook.html')

def Supload(request):
    print("upload")
    print(request.method)
    if request.method=="POST":
             
       f = TextIOWrapper(request.FILES['my_file'].file, encoding=request.encoding)
       print(f)
       data=[]
      
       for row in csv.reader(f):
           data.append(row)
        
       print(data)
    return render(request,'Supload.html')

def lending_books(request):
    print("hello")
    global student_no,card_number,book_number
    context={}
    b=["sname","usn","bname","bid","date_issue","due_date"]
    dt1 = str(datetime.datetime.now())
    date_of_issue=dt1[:10]
    dt2=str(datetime.datetime.today() - datetime.timedelta(days=-15))
    duedate=dt2[:10]
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        #d=request.POST
        book_number=request.POST.get('bk')
        print(book_number)
        student_no=request.POST['usn']
        card_number=request.POST['cardno']
            
        
        s = "insert into lending_book(usn,bookid,date_issue,due_date,cardno) VALUES (%s,%s,%s,%s,%s)"
        val = (student_no,book_number,date_of_issue,duedate,card_number)
         # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
        c="select s.name,s.usn,b.book_id,b.book_name,l.date_issue,l.due_date from student s,book b,lending_book l where s.usn=l.usn and b.book_id=l.bookid;"
        cursor.execute(c)
        result=cursor.fetchall()
        for i in range(len(result)):
            context[i+1]={}
            context[i+1]=dict(zip(b,list(result[i])))
    return render(request,'table1.html',{"data":context})

def deletebook(request):
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="bid":
               book_no=value
        s = "delete from book where book_id='%s'" % (book_no)
       
        # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s)
        m.commit()
    return render(request,'deletebook.html')



def display_book(request):
    print("display")
    context={}
    b=["book_id","book_name","author","price","no_of_copies","publication","edition","sem1","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="Shri@123",database="lib_management")
    cursor=m.cursor()
    
    c="select book_id,book_name,sem1,branch,no_of_copies,publication,edition from book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    m.close()
    return render(request,"table.html", {"data":context})
"""def display_book(request):
    L=select register.cardno,book.book_id,book.bname,book.author,book.publication,book.edition,book.type_of_book,register.date_of_issue,register.due_date FROM register,book where register.id=book.book_id and usn=%s
    db=sql.connector.connect(host="127.0.0.1",user="root",password="n1k2s3s4",database="library")
    cur=db.cursor()
    cur.execute(L,(usn,))
               result=cur.fetchall()
               db.close()
               s1=[row for row in result]
               i=2
           
               for st in s1:
                   for j in range(len(st)):
                       e=tkinter.Label(myframe,width=15,text=st[j],borderwidth=2, relief='ridge',anchor='w',bg='white')
                       e.grid(row=i,column=j)
                       
                   i=i+1

    return render(request,'student_page.html')"""













"""import os
from django.shortcuts import render
from io import TextIOWrapper
from django.http import HttpResponse
import mysql.connector as sql
import datetime
import csv
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def question(request):
    return render(request,'question_paper.html')
def bscience(request):
    return render(request,'basic_science.html')
def comis(request):
    return render(request,'com_is.html')
def mechanical(request):
    return render(request,'mech.html')
def maths(request):
    return render(request,'maths.html')
def civil(request):
    return render(request,'civil.html')
def ec(request):
    return render(request,'ec.html')

def fadmin(request):
    return render(request,'fadmin.html')
def firstadminpg(request):
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="sn":
               sname=value
            if key=="usn":
               sid=value
            if key=="chin":
               checkin=value
            if key=="chout":
                checkout=value
            
            if key=="sem":
               sem1=value
            if key=="year":
               year=value
            if key=="dept":
               branch=value
        s = "insert into log_book(sname,usn,checkin,checkout,sem,year,branch) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (sname,sid,checkin,checkout,sem1,year,branch)
       # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
       
    return render(request,'firstadminpg.html')


def logbook(request):
    context={}
    b=["sname","usn","cin","cout","sem","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
    cursor=m.cursor()
    c="select * from log_book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))



    return render(request,'checkin.html',{"data":context})


    return render(request,'firstadminpg.html')
def adminm(request):
    return render(request,'adminm.html')

def deletebook(request):
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="bid":
               book_no=value
        s = "delete from book where book_id='%s'" % (book_no)
       
        # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s)
        m.commit()




    return render(request,'deletebook.html')
def UpdBook(request):
    global book_name,book_id,author,price,no_of_copies,publication,edition,sem1,year,branch
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="bn":
               book_name=value
            if key=="bid":
               book_id=value
            if key=="an":
               author=value
            if key=="pc":
                price=value
            if key=="nc":
               no_of_copies=value
            if key=="pn":
               publication=value
            if key=="ed":
               edition=value
            if key=="sem":
               sem1=value
            if key=="year":
               year=value
            if key=="dept":
               branch=value
        s = "update book set book_name=%s,author=%s,price=%s,no_of_copies=%s,publication=%s,edition=%s,sem1=%s,year=%s,BRANCH=%s where book_id=%s"
        val = (book_name,author,price,no_of_copies,publication,edition,sem1,year,branch,book_id)
        # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
    return render(request,'UpdBook.html')
def Sregister(request):
    global usn,name,card_no,email,phone_no,sem,department,year,address
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="usn":
               usn=value
            if key=="nm":
               name=value
            if key=="cn":
               card_no=value
            if key=="em":
                email=value
            if key=="pn":
               phone_no=value
            if key=="ad":
               address=value
            if key=="sem":
               sem=value
            if key=="year":
               year=value
            if key=="dept":
               department=value
        s = "insert into student(sname,sid,address,email,phone,cardno,sem,year,branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name,usn,address,email,phone_no,card_no,sem,year,department)
         # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()





    return render(request,'UpdBook.html')

def Sregister(request):
    return render(request,'Sregister.html')
def Stlist(request):
    context={}
    b=["sname","sid","address","email","phone","cardno","sem","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
    cursor=m.cursor()
    c="select *from student"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    
    return render(request,'Stlist.html',{"data":context})
def insertbook(request):
    return render(request,'insertbook.html')



def Supload(request):
    print("upload")
    print(request.method)
    if request.method=="POST":
             
       f = TextIOWrapper(request.FILES['my_file'].file, encoding=request.encoding)
       print(f)
       data=[]
      
       for row in csv.reader(f):
           data.append(row)
        
       print(data)
    return render(request,'Supload.html')
    

def ad_logaction(request):
    global em,pwd
    print("student")
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        
        if em=='keerthi@gmail.com' and pwd=='123':
            return render(request,"adminm.html")
        else:
            return render(request,'error.html')

    return render(request,'admin_login.html')
def insertbook(request):
    global book_name,book_id,author,price,no_of_copies,publication,edition,sem1,year,branch
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="bn":
               book_name=value
            if key=="bi":
               book_id=value
            if key=="an":
               author=value
            if key=="pri":
                price=value
            if key=="noc":
               no_of_copies=value
            if key=="pn":
               publication=value
            if key=="ed":
               edition=value
            if key=="sem1":
               sem1=value
            if key=="year":
               year=value
            if key=="dept":
               branch=value
        s = "insert into book(book_id,book_name,author,price,no_of_copies,publication,edition,sem1,year,branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (book_id,book_name,author,price,no_of_copies,publication,edition,sem1,year,branch)
       # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
    return render(request,'insertbook.html')
def Sregister(request):
    global usn,name,card_no,email,phone_no,sem,department,year,address
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="usn":
               usn=value
            if key=="nm":
               name=value
            if key=="cn":
               card_no=value
            if key=="em":
                email=value
            if key=="pn":
               phone_no=value
            if key=="ad":
               address=value
            if key=="sem":
               sem=value
            if key=="year":
               year=value
            if key=="dept":
               department=value
        s = "insert into student(sname,sid,address,email,phone,cardno,sem,year,branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name,usn,address,email,phone_no,card_no,sem,year,department)
         # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
    return render(request,'Sregister.html')
def student_logaction(request):
    global em,pwd
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from student where email='{}' and sid='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"student_page.html")

    return render(request,'student_login.html')

def display_book(request):
    print("display")
    context={}
    b=["book_id","book_name","author","price","no_of_copies","publication","edition","sem1","year","branch"]
    m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
    cursor=m.cursor()
    
    c="select book_id,book_name,sem1,branch,no_of_copies,publication,edition from book"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    
    return render(request,"table.html", {"data":context})"""
"""def order_details(request):
    now = datetime.datetime.now()
    
    person= {'firstname': 'Priska', 'lastname': 'Kashyap'}
    #item_list = {"Chocolate": 4, "Pen": 10, "Pencil": 3}
    #order_number= "000132342"
    context= {
        'person': person,
        #'item_list': item_list,
        #'order_number': order_number,
        #'current_date': now.date(),
        }
    return render(request, 'sample.html', context)"""
"""def lending_books(request):
    print("hello")
    global student_no,card_number,book_number
    context={}
    b=["sname","usn","bname","bid","date_issue","due_date"]
    dt1 = str(datetime.datetime.now())
    date_of_issue=dt1[:10]
    dt2=str(datetime.datetime.today() - datetime.timedelta(days=-10))
    duedate=dt2[:10]
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
        cursor=m.cursor()
        #d=request.POST
        book_number=request.POST.get('bk')
        print(book_number)
        student_no=request.POST['usn']
        card_number=request.POST['cardno']
            
        
        s = "insert into lending_book(usn,bookid,date_issue,due_date,cardno) VALUES (%s,%s,%s,%s,%s)"
        val = (student_no,book_number,date_of_issue,duedate,card_number)
         # c="insert into signup('{}','{}','{}','{}')".format(name1,userid1,address1,phone1)
        cursor.execute(s,val)
        m.commit()
        c="select sname,sid,book_id,book_name,date_issue,due_date from student,book,lending_book where sid=usn and book_id=bookid;"
        cursor.execute(c)
        result=cursor.fetchall()
        for i in range(len(result)):
            context[i+1]={}
            context[i+1]=dict(zip(b,list(result[i])))
    return render(request,'table1.html',{"data":context})"""
"""def display_lendingbook(request):
    print("display")
    context={}
    b=["sname","usn","bname","bid","date_issue","due_date"]
    m=sql.connect(host="localhost",user="root",passwd="n1k2s3s4",database="website")
    cursor=m.cursor()
    
    c="select sname,sid,book_id,book_name,date_issue,due_date from student,book,lending_book where sid=usn and book_id=bookid;"
    cursor.execute(c)
    result=cursor.fetchall()
    for i in range(len(result)):
        context[i+1]={}
        context[i+1]=dict(zip(b,list(result[i])))
    
    return render(request,"table.html", {"data":context})"""