# 方法一
# from AA import AA
#
# aa = AA(2, 3)
# aa.add()
# 方法二
import AA
import sys
sys.path.append(r'C:\Users\user\PycharmProjects\python-base\py01\hello')
import Test
aa = AA.AA(3, 4)
aa.add()
t = Test.Test()
t.content = '人生苦短，我用python'
t.normal_method()
t.class_method()
t.static_method()