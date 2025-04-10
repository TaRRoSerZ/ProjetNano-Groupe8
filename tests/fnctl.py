# fcntl.py (faux module pour Windows)
def ioctl(fd, op, arg=0, mutate_flag=True):
    return 0