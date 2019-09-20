- lambda 闭包引用
```python
def multipliers():
    return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]
# 结果是 [6, 6,6, 6], 因为函数的闭包。for循环执行结束后。 i最后值为3
```

- 数组的引用
```python
test_list = [[]] * 5
# test_list[0] 和test_list[1] 都是针对同一个地址的引用， id() 输出地址都是一样的
```
