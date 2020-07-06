import ezsheets

HEADER_ROW_NUMBER = 1
MAX_NUMBER_OF_ROWS = 15001

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')


for index, value in enumerate(ss[0].getRows(), start=1):
    if index == HEADER_ROW_NUMBER:
        continue
    if index > MAX_NUMBER_OF_ROWS:
        break
    product_of_rows = int(ss[0].getRow(index)[0]) * int(ss[0].getRow(index)[1])
    if product_of_rows != int(ss[0].getRow(index)[2]):
        print(f"Row number with incorrect total = {index}")
