def gambarField():
    for baris in range(5):
        if baris%2:
            print("-----")
        else:
            for kolom in range(5):
                if kolom%2:
                    print("|", end = "")
                else:
                    if kolom!=4:    
                        print(" ", end = "")
                    else:
                        print(" ")

gambarField()