def clamp(n, n_min, n_max):
    if n < n_min:
        return n_min
    elif n > n_max:
        return n_max
    else:
        return n