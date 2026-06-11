#!/usr/bin/python3
""""""

import requests
import json
import csv

from requests.models import HTTPError


def fetch_and_print_posts():
    """"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        rjson = r.json()
        for post in rjson:
            print(post["title"])


def fetch_and_save_posts():
    """"""
    headers = ["id", "title", "body"]
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        rlist = r.json()
        with open("posts.csv", "w", newline="") as file:
            csvwriter = csv.DictWriter(file, headers)
            csvwriter.writeheader()
            csvwriter.writerows(rlist)
