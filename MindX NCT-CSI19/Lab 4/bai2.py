def reduce_fraction(a, b):
    # Tìm ước chung lớn nhất bằng thuật toán Euclidean
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # Tìm GCD của tử và mẫu
    divisor = gcd(a, b)
    
    # Chia cả tử và mẫu cho GCD
    return a // divisor, b // divisor