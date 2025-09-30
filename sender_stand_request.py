import configuration
import data

import requests

#Creates a user and return token
def create_user():
    response = requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,headers=data.user_data["headers"], json=data.user_data["user_body"])
    return response

def create_kit(name):
    token = create_user().json()["authToken"]
    kit_data = data.kit_data.copy()
    kit_data["headers"]["Authorization"] = f"Bearer {token}"
    kit_data["kit_body"]["name"] = name
    new_kit_data = kit_data
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_KITS_PATH, headers=new_kit_data["headers"], json=new_kit_data["kit_body"])

def get_database_kits(name):
    kit_response = create_kit(name)
    database_records = []

    if kit_response.ok:
        response = requests.get(configuration.URL_SERVICE+configuration.DATABASE_PATH+configuration.TABLES_PATH[0]).text
        for l in response.split('\n'):
            database_records.append(l.split(","))

        database_last_record = database_records[-2]
        return database_last_record[1]
    else:
        return "Not new record"

