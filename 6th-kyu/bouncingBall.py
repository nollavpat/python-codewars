def bouncingBall(h, bounce, window):
    if h <= 0:
        return -1
    if bounce <= 0 or bounce >= 1.0:
        return -1
    if window >= h:
        return -1

    current_height = float(h) * bounce
    count = 1

    while current_height > window:
        current_height *= bounce
        count += 2

    return count