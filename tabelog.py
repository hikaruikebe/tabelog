import mysql.connector
import pdb
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import csv
import pathlib

mydb = mysql.connector.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

csv_path = pathlib.Path.cwd() / "./data/yakitori_east.csv"
dict_list = list()

with csv_path.open(mode="r") as csv_reader:
    csv_reader = csv.reader(csv_reader)
    for rows in csv_reader:
        dict_list.append(
            {
                "store_name": rows[1],
                "store_name_english": rows[2],
                "score": rows[3],
                "review_cnt": rows[4],
                "url": rows[5],
                "url_english": rows[6],
                "address": rows[7],
                "address_english": rows[8],
                "website": rows[9],
            }
        )

# mycursor.execute("CREATE DATABASE IF NOT EXISTS tabelog")
mycursor.execute("USE tabelog")
mycursor.execute(
    """CREATE TABLE IF NOT EXISTS tabelog (
    store_name VARCHAR(255) PRIMARY KEY,
    store_name_english VARCHAR(255),
    score DOUBLE,
    review_cnt INT,
    url VARCHAR(255),
    url_english VARCHAR(255),
    address VARCHAR(255),
    address_english VARCHAR(255),
    website VARCHAR(255)
    )"""
)

for item in dict_list:
    sql = "INSERT IGNORE INTO tabelog (store_name,  store_name_english,  score,  review_cnt,  url,  url_english,  address,  address_english,  website) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
        item["store_name"],
        item["store_name_english"],
        item["score"],
        item["review_cnt"],
        item["url"],
        item["url_english"],
        item["address"],
        item["address_english"],
        item["website"],
    )

    mycursor.execute(sql, val)
mydb.commit()

print("")
