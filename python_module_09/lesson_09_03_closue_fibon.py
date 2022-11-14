def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    return fibonacci
    

if __name__ == "__main__":
    a = caching_fibonacci()
    print(a(10))
        
            
        
            
        
            

        

    