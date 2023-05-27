def Array_reverse(arr):
 
 Results = []

 length = len(arr)
 
 for _ in range(length-1,-1,-1):
  Results.append(arr[_])
 
 return Results


if (__name__=="__main__"):
    print(Array_reverse( [1, 2, 3, 4, 5, 6]))