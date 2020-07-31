from datetime import datetime as dt

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return(int(abs((dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds())))

        
    return (m*60)
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)

        
