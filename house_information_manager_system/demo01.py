"""
    读取csv文件
"""
import csv

with open("house.csv",encoding="utf-8") as csvfile:
    for line in csv.reader(csvfile):
        print(line[1])
        break