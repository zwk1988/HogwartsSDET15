'''课后作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
from decimal import Decimal

import pytest

from 作业.pytest实战.calc import Calc


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calc()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        [1, 1, 2],
        [Decimal('0.2'), Decimal('0.2'), Decimal('0.4')],
        [-10, 5, -5],
        [-2, -8, -10],
        [-0.5, -0.5, -1],
        [100000, 200000, 300000]
    ])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [
        [1, 1, 0],
        [Decimal('0.6'), Decimal('0.2'), Decimal('0.4')],
        [-10, 5, -15],
        [-20, -10, -10],
        [300000, 200000, 100000]
    ])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [
        [1, 0, 0],
        [Decimal('0.5'), Decimal('0.2'), Decimal('0.1')],
        [-10, 5, -50],
        [-10, -10, 100],
        [300000, 200000, 60000000000]
    ])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [
        [1, 0, 0],
        [Decimal('0.5'), Decimal('0.2'), Decimal('2.5')],
        [-10, 5, -2],
        [-10, -10, 1],
        [1000000, 200000, 5]
    ])
    def test_div(self, a, b, expect):
        if b == 0:
            print("除数不能为0")
        else:
            result = self.calc.div(a, b)
            assert result == expect
