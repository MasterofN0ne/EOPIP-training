def delete_dups(arr):
    f, s = 0, 1 

    i = 0

    while i < len(arr):
        if arr[f] == arr[s]:
            arr.remove(f)
            arr.append(0)
        
        f += 1 
        s += 1
        i += 1 
