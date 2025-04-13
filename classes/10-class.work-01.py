# 要求：创建一个名为 Book 的类，包含 title、author 和 pages 三个属性，以及一个返回书籍信息的 get_info 方法。
class Book(object):

    def __init__(self, title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def get_info(self):
        return f"《{self.title}》由作者{self.author}名著，共{self.pages}数页"
result=Book("a","li",900)
print(result.get_info())