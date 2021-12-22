import time



def run_time(func):
    print("run_timeだよ")
    def funcname(*args, **kwargs):
        
        #実行時間 [time.time() - starttrim]
        starttrim = time.time()
        result = func(*args,**kwargs)
        print(f'args:{args} kwargs:{kwargs}')
        print(f'実行関数:{func.__name__} 実行時間:{time.time()-starttrim}')         #実行関数と実行時間を表示

        return result
    print("run_timeの下の方だよ")
    return funcname


# main
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)


test(3)
test(5)
