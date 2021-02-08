#! /usr/bin/env python3
"""using csv data"""
import csv

def main():
    # open the CSV dataset
    with open("vendor.csv","r") as vendorfile:
        vendordata = csv.reader(vendorfile, delimiter=",")
        for row in vendordata:
            print("The IP address "  + row[2] + \
              " requires the driver " + row[3])

main()


  
