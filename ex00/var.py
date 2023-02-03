#!/usr/bin/python3

def my_var():
	v1 = 42
	v2 = "42"
	v3 = "quarante-deux"
	v4 = 42.0
	v5 = True
	v6 = [42]
	v7 = {42: 42}
	v8 = (42,)
	v9 = set()
	print (v1, "has a type", type(v1))
	print (v2, "has a type", type(v2))
	print (v3, "quarante-deux has a type", type(v3))
	print (v4, "has a type", type(v4))
	print (v5, "has a type", type(v5))
	print (v6, "has a type", type(v6))
	print (v7, "has a type", type(v7))
	print (v8, "has a type", type(v8))
	print (v9, "has a type", type(v9))


if __name__ == '__main__':
	my_var()