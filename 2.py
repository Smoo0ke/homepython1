x, y, z = map(int, input().split())

if not (x or y or z) == (not x and not y and not z):
    print("Утверждение не верно.")
else:
    print("Утверждение верно.")
