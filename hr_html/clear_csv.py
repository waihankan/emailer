#!/usr/bin/python3

# this file should be in the same level as *hr_applicants.csv* in order to work properly.
import os
import csv

try:
    os.remove("hr_applicants.csv")
except:
    print("already removed hr_applicants.csv")

with open("hr_applicants.csv", "w+") as file:
	writer = csv.writer(file)
	writer.writerow(["Name", "Email"])
