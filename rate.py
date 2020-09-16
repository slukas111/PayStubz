sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
    print(fh, fr)
except:
    print("Error, Please use number values" )
    quit()
if fh > 40:
    print("Regular + Overtime rate")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    hours = (fh - 40.0)
    xp = reg + otp
    print("Overtime Pay: ", otp, "OvertimeHours: ", hours)
else:
    print("Regular Rate")

    xp = fh * fr
print("Pay", xp)