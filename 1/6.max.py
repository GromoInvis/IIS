print ("programa dlia znahodgennia naibilshogo chisla ")
while True:
    a = float(input("vvedit pershe chislo - "))
    b = float(input("vvedit dryhe chislo - "))
    c = float(input("vvedit tretie chislo - "))
    if a < b:
        max = b
    else:
        max = a
    if max < c:
        max = c
    print ("naibilshe - ", max)
