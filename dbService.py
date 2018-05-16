from pymongo import MongoClient

class dbService():
    def __init__(self,db_name,collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, anyObject):
        try:
            insert_id = self.collection.insert_one(anyObject)
            print "Successfully added details"
        except:
            print "Error occurred while inserting data"

    def find_one(self, id):
        try:
            return self.collection.find_one({"Id":id})
        except:
            print "Error in fetching records for id: %s in collection: %s",id,self.collection
    
    def delete_one(self, id):
        try:
            self.collection.remove({"Id":id})
        except:
            print "Error in deleting records for id:%s in collection: %s",id,self.collection
    
    #return tyype list of objects
    def find_all(self):
        try:
            return self.collection.find()
        except:
            print "Error in getting all records in collection: %s",self.collection

    #return the count of the total documents in the collection
    def get_count(self):
        try:
            return self.collection.count()
        except:
            print "Error in getting the count of the documents in collection: %s",self.collection

    def update_doc(self,updateQuery,userId):
        try:
            return self.collection.update_one({"Id":userId},updateQuery)
        except:
            print "Error in updating document in collection: %s",self.collection

    def end_subscription_update(self,userId, planId, timestamp):
        try:
            return self.collection.update_one(
                {"Id":userId,"plan.planId":planId},
                {'$set': {"plan.$.dateOfTermination":timestamp,"plan.$.isActive":False}
                })
        except:
            print "Error in terminating subscription"