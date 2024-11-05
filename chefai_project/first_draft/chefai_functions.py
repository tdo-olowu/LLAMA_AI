#!/usr/bin/env python3

"""
CHEF AI FUNCTIONS
    say_hello()
    say_goodbye()
    valid(u_prompt)
"""

def say_hello():
    print("Hello, welcome to ChefAI.")
    print("Ask it for cooking advice")

def say_goodbye():
    print("Thanks for using ChefAI! See ya later!")

def valid(u_prompt):
    # not empty
    return (u_prompt != "")
