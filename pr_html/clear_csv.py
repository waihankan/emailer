#!/usr/bin/python3

import os

try:
    os.remove("pr_applicants.csv")
except:
    print("already removed pr_applicants.csv")

file = open("pr_applicants.csv", "w+")
file.close()
