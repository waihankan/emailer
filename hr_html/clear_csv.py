#!/usr/bin/python3

# this file should be in the same level as *applicants.csv* in order to work properly.
import os
import csv

try:
    os.remove("applicants.csv")
except:
    print("already removed applicants.csv")

with open("applicants.csv", "w+") as file:
	writer = csv.writer(file)
	writer.writerow(["Name", "Email"])
