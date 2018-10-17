from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint


collection = connectMongo()

##### FIND ALL ENTRIES IN THE DATABASE #####
# Assuming RQ0 is the query to find all entries in the database
RQ0 = collection.find()

#for data in RQ0:
#  pprint.pprint(data)

######## ADD ENTRIES FROM dummy json to MONGODB #######

with open('dummy-fitness.json', 'r') as json_file:
   json_str = json.load(json_file)

json_data = []
#for i in range(len(json_str)):
#  json_data.append(json_str[i])

#WQ1 = collection.insert_many(json_data)

######## COUNT ENTRIES WITH CONDITION #######
RQ1 = collection.count()

#print(RQ1)

######## FIND ENTRIES WITH CONDITION #######
######## collection.find(CONDITION) #######
######## E.g., collection.find({"Name" : "Alice"}) #######

RQ2 = collection.find({"tags": "irregular"})

#for elem in RQ2:
#  pprint.pprint(elem)

RQ3 = collection.find({"goal.stepGoal":
                     {"$lte": 1500}
                  }
)

#for elem in RQ3:
#  pprint.pprint(elem)
######## UPDATE ENTRIES WITH CONDITION ########
######## collection.update_one(CONDITION, _update_) #######
######## collection.update_many(CONDITION, _update_)
######## E.g., collection.find({"Name" : "Alice"}, {"$inc" : {"age" : 1} })

with open('user1001-new.json', 'r') as json_file:
   data = json.load(json_file)

new_uid = data['uid']
new_height = data['height']
new_weight = data['weight']
new_tags = data['tags']

WQ2 = collection.update_one({"uid": new_uid
                      },
                     {
                        "$set":
                           {"height": new_height, "weight": new_weight, "tags": new_tags
                            }
                     }
)

######## DELETE ENTRIES WITH CONDITION ########
######## collection.delete_one(CONDITION) #######
######## collection.delete_many(CONDITION)
######## E.g., collection.find({"Name" : "Alice"})

######## AGGREGATE ENTRIES WITH PIPELINE ########
######## collection.aggregate(PIPELINE) ########

RQ4 = collection.aggregate([
   {
      "$addFields": {
         "totalActivityDuration": {"$sum": "$activityDuration"}
      }
   }
])
for elem in RQ4:
   pprint.pprint(elem)