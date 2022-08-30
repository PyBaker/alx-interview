def pascal_triangle(n):
    """ Function to return Pascal's Triangle """
    if n <= 0:
        return []
    pascal_list = []
    for i in range(0,n,-1):
        if i == n:
            continue
        pascal_list[0].append(i)
        pascal_list[-1].append(i)
    return pascal_list

