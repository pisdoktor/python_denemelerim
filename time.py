import time

time.sleep(3)

print("3 saniye bekledim")

bugun = time.localtime()

print("Yıllardan", bugun.tm_year)
print("Aylardan", bugun.tm_mon)
print("Günlerden", bugun.tm_mday)
print("Saat tam şuanda", bugun.tm_hour,":", bugun.tm_min)

print("Tarih:",time.strftime("%d/%m/%Y", bugun))