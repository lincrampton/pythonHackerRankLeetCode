def print_rangoli(size):
    from string import ascii_lowercase
    alpha = ascii_lowercase

    arr = []
    for i in range(size):
        line = "-".join(alpha[i:size])
        arr.append((line[::-1]+line[1:]).center(4*n-3, "-"))
    print('\n'.join(arr[:0:-1]+arr))
