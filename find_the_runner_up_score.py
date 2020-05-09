if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = max(arr)
    x = []
    for i in arr:
        if (largest-i) != 0:
            x.append(largest-i)
    if len(x) != 0:
        smallest_diff = min(x)
        print(largest-smallest_diff)
    else:
        print("no runner up")

    

    
