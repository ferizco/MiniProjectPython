import datetime

#input variable
tahun = input("Year: ")
bulan = input("Month: ")
tanggal = input("Day: ")

#change str to int
Ttahun = int(tahun)
Bbulan = int(bulan)
Ttanggal = int(tanggal)

#print the day
y = datetime.datetime(Ttahun, Bbulan, Ttanggal)
print(y.strftime("You are born in %A"))