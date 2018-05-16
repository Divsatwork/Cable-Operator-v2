import web
import mainService

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/payment','payment',
    '/users', 'users',
    '/users/get', 'getUser',
    '/users/new', 'newUser',
    '/users/modify', 'modifyUser',
    '/users/del', 'deleteUser',
    '/users/plans', 'planUser',
    '/users/plans/add', 'addPlanUser',
    '/users/plans/end', 'endPlanUser',
    '/plans', 'plans',
    '/plans/new', 'newPlan',
    '/plans/modify', 'modifyPlan',
    '/plans/del', 'deletePlan'
)

class index:
    def GET(self):
        return render.index(mainService.get_db_content())

class planUser:
    def GET(self):
        return render.user_get()
    
class getUser:
    def GET(self):
        return render.user_get()

    def POST(self):
        return render.user_profile(mainService.get_user_details(web.input()), mainService.get_plan_db_content())

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
        return render.usermain()

class newUser:
    def GET(self):
        return render.user_create()
    
    def POST(self):
        mainService.insert_db(web.input(), 'user')
        return render.success('User added successfully')

class deleteUser:
    def GET(self):
        return render.user_delete()

    def POST(self):
        mainService.delete_object(web.input(),'user')
        return render.success('Object deleted successfully')

class addPlanUser:
    def POST(self):
        mainService.assignPlanToUser(web.input())
        return render.user_profile(mainService.get_user_details(web.input()), mainService.get_plan_db_content())

class modifyUser:
    pass

class endPlanUser:
    def POST(self):
        mainService.end_subscription(web.input())
        return render.user_profile(mainService.get_user_details(web.input()), mainService.get_plan_db_content())


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
