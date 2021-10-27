#!/usr/bin/python3

import os

try:
    os.remove("applicants.csv")
except:
    print("already removed applicants.csv")

file = open("pr_applicants.csv", "w+")
file.close()

