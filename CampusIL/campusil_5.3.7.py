def chocolate_maker(small, big, x):
    """choclate calculator"""
    total = (small * 1) + (big * 5)
    if total >= x:
        print("True")
    else:
        print("False")

chocolate_maker(3, 2, 10)