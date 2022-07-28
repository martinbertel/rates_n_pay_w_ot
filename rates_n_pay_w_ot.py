hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    reg = rate * hours
    tp = (hours - 40.0) * (rate * 0.5)
    pay = reg + tp
else:
   pay = hours * rate
print("Pay:", pay)
