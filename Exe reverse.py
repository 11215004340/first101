def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        reversed_string = reverse_string(s[1:]) + s[0]

    return reversed_string

print(reverse_string("cute miss"))
