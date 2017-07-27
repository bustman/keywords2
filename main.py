import  time

def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        log_pars.debug("%s time %.2f" %(func.__name__,time.clock() - t))
        return res
    return wrapper

def test(self,name):
    self.name = name

while True:
    break
