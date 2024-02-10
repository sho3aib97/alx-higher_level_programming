#!/user/bin/python3
""" read-file function """

def read_file(filename=""):
	""" openning the file """ 
	with open(filename, encoding="utf-8") as f:
		print(f.read(), end='')
