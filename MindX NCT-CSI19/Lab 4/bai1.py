def count_word(inp_str, inp_word):
    # Chuyển cả đoạn văn và từ cần tìm về chữ thường để không phân biệt hoa/thường
    inp_str = inp_str.lower()
    inp_word = inp_word.lower()
    
    # Tách các từ trong đoạn văn
    # Đầu tiên thay thế các dấu câu bằng khoảng trắng
    words = ""
    for char in inp_str:
        if char.isalpha() or char.isspace():
            words += char
        else:
            words += " "
    
    # Tách thành list các từ và đếm số lần xuất hiện của từ cần tìm
    word_list = words.split()
    count = 0
    for word in word_list:
        if word == inp_word:
            count += 1
            
    return count