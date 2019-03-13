+ 1、os.listdir()  遍历目录下所有文件

+ shutil 实现文件的copy以及剪切工作

+ 3、reqeusts上传文件
```
file = {'file': (filename, open(f, 'rb'), 'image/jpeg',)}
 // 文件名，  二进制的文件，  文件类型
 request.post(files=file)
 ```)
 
            
