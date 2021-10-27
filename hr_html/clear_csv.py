#!/usr/bin/python3

# this file should be in the same level as *applicants.csv* in order to work properly.
import os

try:
    os.remove("applicants.csv")
except:
    print("already removed applicants.csv")

file = open("applicants.csv", "w+")
file.close()
