def take(arr,n):
    return arr[slice(0, n)]


# no need for slice
def take(arr,n):
    return arr[:n]

# lambda version
take=lambda a,n:a[:n]
