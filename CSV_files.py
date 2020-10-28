with open("data.csv", "r") as sheet:
    content = sheet.read().splitlines()

    for line in content:
        line_sep = line.split(",")
        print(line_sep[0]+ " is " + line_sep[1] + " years old and " + line_sep[2] + " meters tall " + line_sep[3] + ".")
