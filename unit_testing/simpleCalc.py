from typing import Union, Tuple

class simpleCalc(object):
    @staticmethod
    def add(augend:Union[int,float], addend:Union[int,float]) -> Union[int,float]:
        if type(augend)!=int and type(augend)!=float:
            raise ValueError("The augend must be a int or float.")
        if type(addend)!=int and type(addend)!=float:
            raise ValueError("The addend must be a int or float.")
        return (augend + addend)

    @staticmethod
    def subtract(minuend:Union[int,float], subtrahend:Union[int,float]) -> Union[int,float]:
        if type(minuend)!=int and type(minuend)!=float:
            raise ValueError("The minuend must be a int or float.")
        if type(subtrahend)!=int and type(subtrahend)!=float:
            raise ValueError("The subtrahend must be a int or float.")
        return (minuend - subtrahend)

    @staticmethod
    def multiply(multiplicand:Union[int,float], multiplier:Union[int,float]) -> Union[int,float]:
        if type(multiplicand)!=int and type(multiplicand)!=float:
            raise ValueError("The multiplicand must be a int or float.")
        if type(multiplier)!=int and type(multiplier)!=float:
            raise ValueError("The multiplier must be a int or float.")
        return (multiplicand * multiplier)

    @staticmethod
    def divide(dividend:Union[int,float], divisor:Union[int,float]) -> Tuple[Union[int,float], Union[int,float]]:
        if type(dividend)!=int and type(dividend)!=float:
            raise ValueError("The dividend must be a int or float.")
        if type(divisor)!=int and type(divisor)!=float:
            raise ValueError("The divisor must be a int or float.")
        if divisor == 0:
            raise ZeroDivisionError("The divisor can NOT be 0.")
        quotient = dividend // divisor
        remainder = dividend % divisor
        return (quotient, remainder)