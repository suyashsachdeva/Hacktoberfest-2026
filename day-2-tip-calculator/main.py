print("welcome to tipcalculator")
bill=int(input("What was total bill$ ?\n"))
tip_percent=float(input("What percentage tip would you like to give 10%, 12% or 15% ?  \n"))
distribution=int(input("How many people to split the bill?\n"))
tip=(bill/distribution)*(1+(tip_percent/100))
ftip= round(tip,2)
print(f"Each person should pay ${ftip}")
