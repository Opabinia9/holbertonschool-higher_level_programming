#!/usr/bin/python3
"""Module: fetch posts from jsonplaceholder."""

import requests
import csv


def fetch_and_print_posts() -> None:
    """Fetch and print post titles from jsonplaceholder."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        rjson = r.json()
        for post in rjson:
            print(post["title"])


def fetch_and_save_posts() -> None:
    """Save post data from jsonplaceholder to csv file."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()
        fields = ["id", "title", "body"]
        csvlist = [
            {
                fields[0]: post[fields[0]],
                fields[1]: post[fields[1]],
                fields[2]: post[fields[2]],
            }
            for post in posts
        ]
        with open("posts.csv", "w", newline="") as file:
            csvwriter = csv.DictWriter(file, fields)
            csvwriter.writeheader()
            csvwriter.writerows(csvlist)
