#  Find the Runner-Up Score!

    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = float('-inf');
    mx = max(arr);
    
    for i in range(0,n):
        if(arr[i] >= ans) and arr[i] != mx:
            ans = arr[i];
            
    print(ans);
