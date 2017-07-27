"""
 数据校验
 事务处理(这里的事务类似于数据库事务，意味着要么所有步骤都成功完成，要么事务
失败) 
 缓存
 日志 
 监控 
 调试
 业务规则 
 压缩 
 加密
"""

def fab(n):
    return n if n in (0,1) else fab(n - 1) + fab(n - 2)


from functools import partial, wraps
from timeit import Timer

p = partial(fab, 30)
t = Timer(p)
print(t.timeit(number=3))

def memoize(fn):
    known = {}
    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = '.'.join([str(args), str(kwargs)])
        if key in known:
            return known[key]
        else:
            known[key] = fn(*args, **kwargs)
            return known[key]
    return wrapper

@memoize
def fab(n):
    return n if n in (0,1 ) else fab(n-1) + fab(n-2)
p = partial(fab, 30)
t = Timer(p)
print(t.timeit(number=3))
