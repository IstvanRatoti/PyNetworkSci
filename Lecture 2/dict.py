name2num = {}
name2num["ELTE"] = 1635	# Dictionary: key - value pair
name2num["MTA"] = 1825

print(name2num)

#name2num["BME"] += 1

print(name2num.keys())
print(name2num.values())

if "CEU" not in name2num:
	print("CEU not in keys")
