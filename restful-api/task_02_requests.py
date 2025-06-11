#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder.
    """
    rep = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"Status Code: {rep.status_code}")

    if rep.status_code == 200:
        post = rep.json()
        print(post['title'])

def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder
    """
    rep = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {rep.status_code}")

    if rep.status_code == 200:
        posts = rep.json()
        posts_to_save = []
        for post in posts:
            post_data = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts_to_save.append(post_data)
        with open("posts.csv", mode="w", newline='', encoding="utf-8") as fichier_csv:
            col = ['id', 'title', 'body']
            writer = csv.DictWriter(fichier_csv, fieldnames=col)
            writer.writeheader()
            writer.writerows(posts_to_save)
