import delay_file
def delay_avg(n):
    x=0
    for i in range(n):
        x+=delay_file.delay_()
    return x/n
    