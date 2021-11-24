#!/usr/bin/python3

import os
import csv

try:
    os.remove("agreement_applicants.csv")
except:
    print("already removed agreement_applicants.csv")

with open("agreement_applicants.csv", "w+") as file:
    writer = csv.writer(file)
    writer.writerow(["Email", "Time"])
    
