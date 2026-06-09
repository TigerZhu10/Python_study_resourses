

def mult(num_1, num_2):
    return num_1,num_2,num_1*num_2

n_1, n_2, result = mult(10,7)
print(n_1)
print(n_2)
print(result)


def create_dict(n1, n2):
    dict = {"first" : n1, "second" : n2}
    return dict
catch_dict = create_dict(2,3)