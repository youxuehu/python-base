class Test:
    name = 'python'
    content = '人生苦短，及时行乐'

    def normal_method(self):  # 普通方法
        print(self.content)

    @classmethod
    def class_method(cls):  # 类方法
        print(cls.content)

    @staticmethod
    def static_method():  # 静态方法
        print('content')


t = Test()
t.content = '人生苦短，我用python'
t.normal_method()
t.class_method()
t.static_method()
