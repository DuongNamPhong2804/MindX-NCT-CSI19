def check_substring(str1, str2):
    # Tạo dictionary đếm tần suất ký tự trong str1
    freq1 = {}
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
    
    # Kiểm tra xem có đủ ký tự trong str1 để tạo thành str2 không
    for char in str2:
        if char not in freq1 or freq1[char] == 0:
            return False
        freq1[char] -= 1
    
    return True