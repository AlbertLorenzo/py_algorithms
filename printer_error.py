def printer_error(s):
	n_err = 0
	letters_list = "a b c d e f g h i j k l m"
	for i in s:
		if i not in letters_list:
			n_err += 1
	return str(n_err) + "/" + str(len(s)) 

print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))