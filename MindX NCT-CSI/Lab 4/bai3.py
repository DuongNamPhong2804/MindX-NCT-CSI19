def fibonacci(n):
    # Sử dụng memoization để lưu trữ các kết quả đã tính
    memo = {}
    
    def fib(n):
        # Nếu đã tính trước đó, trả về kết quả
        if n in memo:
            return memo[n]
        
        # Các trường hợp cơ bản
        if n <= 2:
            return 1
            
        # Tính F(n) = F(n-1) + F(n-2)
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
        
    return fib(n)