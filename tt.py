goods_list=[]

import sqlite3
goods_db_conn = sqlite3.connect('food_db')
goods_db_cur = goods_db_conn.cursor()
for i in range(0, len(goods_list)):
    goods_db_cur.execute(
        '''INSERT INTO FOODLIST (TYPE,PRICE,PRIORITY,POSTTIME,EDITEDTIME) VALUES ("{}",{},{},"{}","{}")'''
        .format(goods_list[i]["TYPE"], goods_list[i]["PRICE"],
                goods_list[i]["PRIORITY"], goods_list[i]["POSTTIME"],
                goods_list[i]["EDITEDTIME"]))
goods_db_conn.commit()
goods_db_conn.close()


import requests

# Replace YOUR_ACCESS_TOKEN with a valid access token for the Facebook Graph API
access_token = 'YOUR_ACCESS_TOKEN'

# Specify the endpoint for the Facebook Graph API
endpoint = 'https://graph.facebook.com/v7.0/me'

# Define the parameters for the API request
parameters = {'fields': 'id,name,likes', 'access_token': access_token}

# Send the request to the API
response = requests.get(endpoint, params=parameters)

# Print the JSON response
print(response.json())
