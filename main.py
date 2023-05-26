import requests
import json
import sqlite3

con = sqlite3.connect("example.db")
cursor = con.cursor()
create_table = """
CREATE TABLE IF NOT EXISTS my_dog(id INTEGER PRIMARY KEY, link TEXT, status TEXT)
"""
cursor.execute(create_table)


response = requests.get("https://dog.ceo/api/breeds/image/random")

print(response.status_code)
print(response.headers)
print(response.text)

with open("dog.json", "w") as file:
    json.dump(response.json(), file)

print(response.json()["status"])

link = response.json()["message"]
status = response.json()["status"]
insert_data = "INSERT INTO my_dog(link, status) VALUES(?,?)"
cursor.execute(insert_data, (link, status))
con.commit()
con.close()