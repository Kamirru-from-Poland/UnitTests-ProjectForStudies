def oblicz_pierwiastki(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2

if __name__ == '__main__':
    postac_ogolna = (1,6,8)
    print(oblicz_pierwiastki(*postac_ogolna))