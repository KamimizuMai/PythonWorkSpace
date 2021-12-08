# https://docs.python.org/ja/3.7/library/inspect.html#module-inspect

import inspect

def func():
    pass

result = inspect.getmembers(func)

for k,v in result:
    print(f'{k}=>{v}')