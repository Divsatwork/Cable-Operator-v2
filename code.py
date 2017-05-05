import web,mysql.connector
render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/payment','payment',
    '/users', 'users',
    '/new', 'new',
    '/modify', 'modify',
    '/del', 'delete',
    '/table', 'table'
)

global conn
global cursor
conn=mysql.connector.connect(host='localhost', database='shop', user='root', password='')
if conn.is_connected():
    print "Connection established"
else:
    print "Connection Unsuccesfull"
    exit()
cursor=conn.cursor()


class index:
    def GET(self):
        return render.index()

class payment:
    
    def GET(self):
        form=web.input(user="")
        return render.payment(form.user)

    def POST(self):
        form = web.input(user="", amt=0) #user is VC number and amt is the amount paid by the user
        def pay(user,amt):
            print "Inserted Successfully"
        pay(form.user,form.amt) #call the function to insert into database
    	return render.success()

class users:
    def GET(self):
        return render.usersmain()

class new:
    def GET(self):
        return render.adduser()

    def POST(self):
        form= web.input(user="", cust_name="", cust_no1="", cust_no2="", pack="" )
        print form.user,form.cust_name,form.cust_no1,form.cust_no2,form.pack
        #to insert the customer into the cust table
        def insert(vc,name,no1,no2,pack):
            #to insert the customer and its details
            if no2:
                query="insert into cust values('"+vc+"','"+name+"',"+no1+","+no2+",'Indore')" 
            else:
                query="insert into cust values('"+vc+"','"+name+"',"+no1+",null,'Indore')" 
            #cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
            print 'Inserted Successfully'
        insert(form.user,form.cust_name,form.cust_no1,form.cust_no2,form.pack)
        return render.addsuccess()

class delete:
    def GET(self):
        form=web.input(user="")
        return render.deluser(form.user)

    def POST(self):
        form = web.input(user="")
        def remove(vc):
            #to delete the user
            query="delete from cust where VC_No = '"+vc+"';"
            cursor.execute(query)
            conn.commit()
            conn.close()
            print "deleted"
        remove(form.user)
        return render.delsuccess()

class table:
    def GET(self):
        query="select cust.vc_no,cust.name,balance.balance,cust.mob1 from cust,balance,pcust where active_or_past=1 and cust.VC_no=balance.vc_no and cust.vc_no=pcust.vc_no"
        cursor.execute(query)
        rows=cursor.fetchall()
        return render.table(rows)

    def POST(self):
        return true

class modify:
    def GET(self):
        return render.modifyuser()

    def POST(self):
        form = web.input(user="",)#user = vc
        return render.modifysuccess()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
