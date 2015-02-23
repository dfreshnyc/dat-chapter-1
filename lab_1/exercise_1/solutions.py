numbers = [33,66,99,1,2,3,4,5,6]

def is_div33(x):
	return (x % 33) == 0

new_list = filter(is_div33, numbers)

print new_list
