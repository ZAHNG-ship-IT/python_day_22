from pathlib import Path
#
# path = Path('d:/Users/21862/PycharmProject/PythonProject/练习/pi.txt')
# contents_1 = path.read_text()
# print(contents_1)
path = Path(r'd:\Users\21862\PycharmProjects\PythonProject\练习\pi.word.txt')#\Users\21862\PycharmProjects\PythonProject\练习\
if path.exists():
    contents = path.read_text(encoding='utf-8')
    print(contents)####成功啦！！！！
else:
    print(f"文件不存在于：{path.resolve()}")

    ###有隐藏拓展名字
