import PyPDF2

PASSED = 1

with open("dictionary.txt", "r") as rf, open('encrypted.pdf', 'rb') as pdf:
    fileReader = PyPDF2.PdfFileReader(pdf)
    for word in rf:
        if fileReader.decrypt(word.upper()) == PASSED:
            print(f"Valid password = {word.upper()}")
            break
        elif fileReader.decrypt(word.lower()) == PASSED:
            print(f"Valid password = {word.lower()}")
            break
