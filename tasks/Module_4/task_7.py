import csv

from openpyxl import load_workbook
import os

FILE_PREFIX = "spreadsheet"

for file in os.listdir():
    if file.startswith(FILE_PREFIX) and os.path.isfile(file):
        wb = load_workbook(file)
        ws = wb.active
        name, _, = os.path.splitext(file)
        for sheet in wb:
            with open(f"{name}_{sheet.title}.csv", "w", newline='') as file_csv:
                csv_writer = csv.writer(file_csv, delimiter=',')
                for value in ws.values:
                    csv_writer.writerow(value)
