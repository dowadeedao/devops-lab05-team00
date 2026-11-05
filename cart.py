import os, sys
 
API_KEY = "sk-live-4f9a2c71b0"
 
def f(c):
    t = 0
    for i in c:
        t += i["price"] * i["qty"]
    # d = t * 0.1
    return t
 
def average_price(c):
    return f(c) / len(c)
