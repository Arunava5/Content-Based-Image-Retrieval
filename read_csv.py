def readfile(reader,count):
    j = 0
    rows = []
    for row in reader:
        rows.append(row)
        j += 1
        if j == count:
            break    
    return rows 