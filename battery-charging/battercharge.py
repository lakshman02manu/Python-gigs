import psutil
def secs2hours(secs):
    mm,ss = divmod(secs,60)
    hh, mm= divmod(mm,60)
    return "%d:%02d:%02d" % (hh,mm,ss)
battery = psutil.sensors_battery()
print("charge = ",battery.percent)
print("Time Left = ",secs2hours(battery.secsleft))
