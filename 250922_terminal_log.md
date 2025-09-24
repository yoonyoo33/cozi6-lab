# 터미널 실행 기록 예시

```
PS C:\Users\YOONYOO> python hello.py
C:\Users\YOONYOO\anaconda3\python.exe: can't open file 'C:\\Users\\YOle or directory

PS C:\Users\YOONYOO> dir
(여러 폴더/파일 목록...)

PS C:\Users\YOONYOO\OneDrive\Escritorio> pyhon hello.py
pyhon : 'pyhon' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는
. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 
(오타로 인한 에러 메시지...)

PS C:\Users\YOONYOO\OneDrive\Escritorio> python hello.py
hello,world

PS C:\Users\YOONYOO\Desktop\파이썬꼬꼬마> python hello.py
hello,world
Traceback (most recent call last):
  File "C:\Users\YOONYOO\Desktop\파이썬꼬꼬마\hello.py", line 15, in <module>
    write_journal()
  File "C:\Users\YOONYOO\Desktop\파이썬꼬꼬마\hello.py", line 4, in write_journal
    today = datetime.now().strftime("%Y-%m-%d")
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?

PS C:\Users\YOONYOO\Desktop\파이썬꼬꼬마> python hello.py
hello,world
오늘의 글을 적어주세요: 색다른 기분이다. 낯설고 또 신기하기도 하고. 이게 정말 저장이 되는걸까?
저장 완료! journal.txt 파일에서 확인해보세요. 📖

PS C:\Users\YOONYOO\Desktop\파이썬꼬꼬마> pip install pypandoc
Collecting pypandoc
  Downloading pypandoc-1.15-py3-none-any.whl.metadata (16 kB)
Downloading pypandoc-1.15-py3-none-any.whl (21 kB)
Installing collected packages: pypandoc
Successfully installed pypandoc-1.15

PS C:\Users\YOONYOO\Desktop\파이썬꼬꼬마> pandoc --version
pandoc.exe 2.12
Compiled with pandoc-types 1.22, texmath 0.12.1.1, skylighting 0.10.4,
citeproc 0.3.0.8, ipynb 0.1.0.1
User data directory: C:\Users\YOONYOO\AppData\Roaming\pandoc
Copyright (C) 2006-2021 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
```