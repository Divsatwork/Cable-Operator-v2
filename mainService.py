from dbService import dbService as DBServer
from datetime import date as dt

myUserdb=DBServer('test','CRMdb')
myPlandb=DBServer('test','Plandb')

def get_db_content():
    return myUserdb.find_all()

#Returns the User Entity to be saved into the database.
def getUserEntity(user_details):
    user = {}
    user['Id'] = str(myUserdb.get_count()+1)
    user['userName'] = user_details['userName']
    user['balance'] = int(user_details.get('balace',0))
    user['contact'] = user_details['userContact']
    user['doc'] = user_details['doc']
    user['isCustomer'] = True
    user['email'] = user_details.get('userEmail',None)
    user['dateOfCreation'] = dt.today()
    user['address'] = user_details['userAddress']
    user['others'] = ''
    user['plan'] = []
    return user

#Insert operation for the db
def insert_db(web_input, memberType):
    if memberType=='user':
        myUserdb.insert(getUserEntity(web_input))
    else:
        myPlandb.insert('this')
    
def get_plan_db_content():
    return myPlandb.find_all()

def delete_object(web_input,memberType):
    if memberType == 'user':
        myUserdb.delete_one(str(web_input['userId']))

def get_user_details(web_input):
    return myUserdb.find_one(str(web_input['userId']))

def get_plan_id(plan_name):
    return str(myPlandb.find_one(str(plan_name).lower())['returnId'])

def get_last_instance(userId, plan_name):
    userInfo = myUserdb.find_one(str(userId))
    inst = 0
    for i in userInfo['plan']:
        if i['planName'] == plan_name:
            inst+=1
    return str(inst+1)

def assignPlanToUser(web_input):
    #update the plans list over here
    planId = web_input['userId']+'-'+get_plan_id(web_input['myPlanList'])+'-'+get_last_instance(web_input['userId'],web_input['myPlanList'])
    query= {
            '$push': {
                'plan': {
                'planName': web_input['myPlanList'],
                'planId': planId,
                'dateOfSubscription' : dt.today(),
                'isActive' : True
                        }
                    }
            }
    myUserdb.update_doc(web_input['userId'], query)

def end_subscription(web_input):
    myUserdb.end_subscription_update(web_input['userId'],web_input['planId'],dt.today())