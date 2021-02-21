[toc]

### Asynchrony（同步） vs Asynchronous（异步）vs Coroutine（协程）

Every asyncio program has at least one event loop. 

The *await* keyword suspends the execution of the current coroutine, and calls the specified awaitable.

Coroutine是比线程更轻量化的存在，像一个进程可以拥有多个线程一样，一个线程也可以拥有多个协程最重要的是，协程不是被操作系统内核所管理，而完全是由程序所控制

https://www.cnblogs.com/dbf-/p/11143349.html

https://stackabuse.com/overview-of-async-io-in-python-3-7/

https://www.jianshu.com/p/84df78d3225a

https://www.cnblogs.com/tashanzhishi/p/10774515.html

https://djangostars.com/blog/asynchronous-programming-in-python-asyncio/

https://www.capitalone.com/tech/software-engineering/async-processing-in-python-for-faster-data-pipelines/

https://docs.python.org/3/library/asyncio-task.html

https://stackabuse.com/python-async-await-tutorial/

### Inheritance and Composition

(略)

### Unit Test and Test Cases

* Unit Test: A unit test verifies that one specific aspect of a fundtion's behaviro is correct
* Test Case: A test case is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle.

*Pytest* expects our tests to be located in files whose names begin with `test_` or end with `_test.py`

```python
# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
```

```python
# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
```

*pytest fixture* helps us set up some helper code that should run before any tests are executed, and are perfect for setting-up resources that are needed by the tests.

```python
# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
```



### Decorator

一切皆对象，我们在开发过程中定义的变量、方程、类、实例等都是对象，并且这些对象是可以传递的，对象间的可传递性可以为我们实现一个“闭包”，而“闭包”就是实现一个装饰器的基础。装饰器可以在不修改原方法的情况下，给方法增加额外的功能。

***闭包：在Python中允许在一个方法中嵌套另一个方法，这种特殊的机制***

假设我们实现一个统计方法执行时间的方程。

```python
import time

def hello():
    start = time.time()
    time.sleep(1)
    print("hello")
    end = time.time()
    print("duration time: %ds" % int(end - start))
   
hello()
```

```
hello
duration time: 1s
```

将时间统计逻辑抽离出来定义一个方程

```python
import time

def timeit(func):   # 计算方法耗时的通用方法
    start = time.time()
    func()          # 执行方法
    end = time.time()
    print("duration time: %ds" % int(end - start))

def hello():
    time.sleep(1)
    print("hello")

timeit(hello) 

timeit(func1)   # 计算func1执行时间
timeit(func2)   # 计算func2执行时间
```

```
hello
duration time: 1s
```

将```hello()```加入时间统计逻辑，不需将```hello()```导入```timeit```，直接调用```hello()```即可

```python
import time

def timeit(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("duration time: %ds" % int(end - start))
    return inner

def hello():
    time.sleep(1)
    print("hello")

hello = timeit(hello)   # 重新定义hello
hello()       # 像调用原始方法一样使用

```

```
hello
duration time: 1s
```

使用decorator装饰器可以实现同样的效果

```python
import time

def timeit(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("duration time: %ds" % int(end - start))
    return inner

@timeit   # 相当于 hello = timeit(hello)
def hello():
    time.sleep(1)
    print('hello')

hello()  # 直接调用原方法即可
```

装饰带参数的方法和带参数的装饰器

```python
import time
from functools import wraps

def timeit(prefix):  # 装饰器可传入参数
    def decorator(func): # 多一层方法嵌套
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print('%s: duration time: %ds' % (prefix, int(end - start)))
        return wrapper
    return decorator

@timeit('prefix1')
def hello(name):
    time.sleep(1)
    print('hello %s' % name)
    
hello('daniel')
```

```
hello daniel
prefix1: duration time: 1s
```

```python
@timeit('prefix2')
def say(name, age):
    time.sleep(1)
    print('hello %s %s' % (name, age))

say('Jack', 23)
```

```
hello Jack 23
prefix2: duration time: 1s
```

知道了如何实现一个装饰器，那么我们可以在不修改原方法的情况下，给方法增加额外的功能，这就非常适合给方法集成一些通用的逻辑，例如记录日志、记录执行耗时、本地缓存、路由映射等功能。

路由映射案例

```python
class Router(object):

    def __init__(self):
        self.url_map = {}

    def register(self, url):
        def wrapper(func):
            self.url_map[url] = func
        return wrapper

    def call(self, url):
        func = self.url_map.get(url)
        if not func:
            raise ValueError('No url function: %s', url)
        return func()

router = Router()

@router.register('/page1')
def page1():
    return 'this is page1'

@router.register('/page2')
def page2():
    return 'this is page2'

print(router.call('/page1'))
```

```
this is page1
```

```python
print(router.call('/page2'))
```

```
this is page2
```





### Method Type

class method vs static method vs instance method 

![](https://pic4.zhimg.com/80/v2-1885610a5b3f3a0c3042d72ecb6e0379_1440w.jpg?source=1940ef5c)

测试文章

1、https://segmentfault.com/a/1190000022900834?utm_source=sf-related

2、单元测试 vs 集成测试 vs 系统测试 vs 验收测试： https://segmentfault.com/a/1190000009358979?utm_source=sf-related

3、装饰器：https://zhuanlan.zhihu.com/p/305604008



