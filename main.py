hobi = []
stop = False
i = 0

while (not stop):
    hobi_baru = input("masukkan hobi yang ke {}: ".format(i))
    hobi.append(hobi_baru)

    i += 1

    tanya = input("mau isi lagi (y/t): ")
    if(tanya == "t"):
        stop = True

    print("kamu memiliki {} hobi".format(len(hobi)))
    for hb in hobi:
        print("- {}".format(hb))