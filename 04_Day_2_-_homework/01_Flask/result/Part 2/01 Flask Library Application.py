from flask import Flask, request, redirect, render_template_string
import psycopg2

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        database="library",
        user="postgres",
        password="coderslab",
        host="127.0.0.1"
    )