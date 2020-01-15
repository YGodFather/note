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

- 多进程
```python
import multiprocessing
import os
import time
import queue
class Producer(multiprocessing.Process):

    def __init__(self, queue, picture_dir):
        super().__init__()
        self.queue = queue
        self.picture_dir = picture_dir

    def run(self) -> None:
        filenames = (filename for filename in os.listdir(self.picture_dir))
        for filename in filenames:
            filename_ = os.path.join(self.picture_dir, filename)
            self.queue.put(filename_)

class Customer(multiprocessing.Process):
    vn1_url = ''

    def __init__(self, queue, name):
        super().__init__(name=name)
        self.queue = queue
        self.num = 0
        self.data = dict(
            pictureBase64='',
            repoIDs=[1, 2],
            limit=10,
            threshold=10,
        )

    def log_print(self, start_time, num):
        if num % 100 == 0:
            now_time = time.time()
            handle_count = round(100 / (now_time - start_time), 2)
            print('{} 已处理的图片数\t{}\t 处理的速度{}张/s'.format(self.name, num, handle_count))
            return now_time
        return start_time

    def run(self) -> None:
        start_time = time.time()
        result_txt = '{}.txt'.format(os.path.join(RESULT_STORE_PATH, self.name))
        while True:
            try:
                with open(result_txt, 'a+', encoding='utf-8') as outfile:
                    capture_path = self.queue.get(timeout=60 * 5)
                    picture_base64 = encode_picture2base64(capture_path)
                    self.data['pictureBase64'] = picture_base64
                    resp = requests.post(url=Customer.vn1_url, cookies=cookies, json=self.data)
                    outfile.write('{}\t{}\n'.format(capture_path, resp.text))
                    self.num += 1
                    start_time = self.log_print(start_time, self.num)
            except queue.Empty:
                print('队列执行结束了', self.name)
                break
            except ConnectionError as e:
                with open('error.txt') as outfile:
                    outfile.write('{}\t{}\n'.format(capture_path, str(e)))
                continue

```