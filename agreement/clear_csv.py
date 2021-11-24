#!/usr/bin/python3

import os

try:
    os.remove("academic_applicants.csv")
except:
    print("already removed academic_applicants.csv")

file = open("academic_applicants.csv", "w+")
file.close()
