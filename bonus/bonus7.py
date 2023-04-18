filenames = ["1.doc", "2.reports", "3.presentation"]
print(filenames)
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]
print(filenames)