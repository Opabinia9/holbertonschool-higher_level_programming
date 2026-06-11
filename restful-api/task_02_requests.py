#!/usr/bin/python3
""""""

import requests
import json
import csv


def fetch_and_print_posts():
    """"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(r.status_code)

    if r.status_code == 200:
        rjson = r.json()
        for post in rjson:
            print(post["title"])


def fetch_and_save_posts():
    """"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        rlist = r.json()
        with open("posts.csv", "w", newline="") as file:
            csvwriter = csv.DictWriter(file, rlist[0].keys())
            csvwriter.writerows(rlist)
