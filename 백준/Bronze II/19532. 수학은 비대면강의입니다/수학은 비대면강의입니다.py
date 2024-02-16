a, b, c, d, e, f = map(int, input().split())
if a == b == d == e == 0 :
    print(0, 0)
    exit(1)

temp_a, temp_b, temp_c, temp_d, temp_e = a, b, c, d, e

if temp_a != 0 and temp_d != 0 :
    a *= temp_d
    b *= temp_d
    c *= temp_d
    d *= temp_a
    e *= temp_a
    f *= temp_a

    temp_x = a - d
    temp_y = b - e
    temp_o = c - f

    if temp_y != 0 :
        y = temp_o // temp_y
        if temp_a != 0 :
            x = (temp_c - (temp_b * y)) // temp_a
        else :
            x = 0
    else :
        y = 0
        if temp_x == 0 :
            x = 0
        else :
            if temp_a != 0 :
                x = temp_c // temp_a
            else :
                x = 0

else :
    a *= temp_e
    b *= temp_e
    c *= temp_e
    d *= temp_b
    e *= temp_b
    f *= temp_b
    
    temp_x = a - d
    temp_y = b - e
    temp_o = c - f

    if temp_x != 0 :
        x = temp_o // temp_x
        if temp_b != 0 :
            y = (temp_c - (temp_a * x)) // temp_b
        else :
            y = 0
    else :
        x = 0
        if temp_y == 0 :
            y = 0
        else :
            if temp_b != 0 :
                y = temp_c // temp_b
            else :
                y = 0

print(x, y)