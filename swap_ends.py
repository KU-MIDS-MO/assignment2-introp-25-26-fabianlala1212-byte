def swap_ends(L, k):
    if not L or k<=0 or k>len(L) // 2:
        return (L.copy(), 0)
    new_list = L[-k:] + L[k:len(L)-k] + L[:k]
    num_swap= k
    return(new_list , num_swap)
print(swap_ends([10,20,40,50,60,70,80], 3))