import importlib
import sys


# 动态导入hello,反射a属性

def test_tmp():
    sys.path.append(".")
    c = importlib.import_module("hello")
    getattr(c, 'a')()
