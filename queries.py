from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint


collection = connectMongo()

##### FIND ALL ENTRIES IN THE DATABASE #####
# Assuming RQ0 is the query to find all entries in the database
# print all the entries in thed database, we just name every entry as RQ0 and print its own data
RQ0 = collection.find()
#for data in RQ0:
#	pprint.pprint(data)
 
with open('dummy-fitness.json', 'r') as json_file:
   json_str = json.load(json_file)

json_data = []
for i in range(len(json_str)):
   json_data.append(json_str[i])

RQ1 = collection.count
#print(RQ1)


RQ2 = collection.find({"tags" : "regular"})

#for elem in RQ2:
#  pprint.pprint(elem)

 
RQ3 = collection.find({"goal.stepGoal":
                     {"$lte": 1500}
                  }
)
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
							{"height":new_height, "weight": new_weight, "tags": new_tags
							}
					}
)

 
RQ4 = collection.aggregate([
   {
      "$addFields": {
         "totalActivityDuration": {"$sum": "$activityDuration"}
      }
   }
])

for elem in RQ4:
   pprint.pprint(elem)











