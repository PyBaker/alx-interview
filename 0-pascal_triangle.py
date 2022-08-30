def pascal_triangle(n):
    """ Function to return Pascal's Triangle """
    if n <= 0:
        return []
    pascal_list = []
    print(pascal_list)
    for i in range(n,-1,-1):
        if i == n:
            continue
        pascal_list.insert(0,i)
        pascal_list.insert(-1,i)
        print(pascal_list)
    return pascal_list

print(pascal_triangle(5))
