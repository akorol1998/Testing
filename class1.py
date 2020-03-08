
class myClass():
    ''' This class is contains four static methods that perform arithmetic
    computations based on the single argument that is parsed to as a paramter to
	method call. The purpose this class serves is completely educational has the aim 
    to help student grasp meaning of writing documentation/description of the class/method'''

    @staticmethod
    def computeFirst(x: float) -> float:
        ''' This method takes an argument of type float and performs following computations:
        y=x^4*4.769+x^3*4.159-x^2*2.745+x*4.503
        value of an rgument should be in range of(-inf,2.853] and [88.069, +inf) '''

        try:
            if x > 2.853 and x < 88.069:
                raise ValueError
            y = x**(4*4.769) + x**(3*4.159) - x**(2*2.745) + x*3.317
        except TypeError as error:
            print(f"You got an {error}\nYou need float type")
            y = None
        except ValueError as error:
            print(f"You got Wrong value {error}\n value should be in range of(-inf,2.853] and [88.069, +inf) float type")
            y = None
        return y

    @staticmethod
    def computeSecond(x: float) -> float:
        ''' This method takes an argument of type float and performs following computations:
        y=x^3*2.027-x^2*2.578+x*6.966
        value of an rgument should be in range of(-inf,2.853] and [88.069, +inf) '''
        try:
            if x > 2.853 and x < 88.069:
                raise ValueError
            y = x**(3*2.027)-x**(2*2.578)+x*6.966
        except TypeError as error:
            print(f"You got an {error}\nYou need float type")
            y = None
        except ValueError as error:
            print(f"You got Wrong value {error}\n value should be in range of(-inf,2.853] and [88.069, +inf) float type")
            y = None
        return y

    @staticmethod
    def computeThird(x: float) -> float:
        ''' This method takes an argument of type float and performs following computations:
        y=x^2*1.575+x*3.894
        value of an rgument should be in range of(-inf,2.853] and [88.069, +inf) '''
        try:
            if x > 2.853 and x < 88.069:
                raise ValueError
            y = x**(2*1.575)+x*3.894
        except TypeError as error:
            print(f"You got an {error}\nYou need float type")
            y = None
        except ValueError as error:
            print(f"You got Wrong value {error}\n value should be in range of(-inf,2.853] and [88.069, +inf) float type")
            y = None
        return y
    
    @staticmethod
    def computeFourth(x: float) -> float:
        ''' This method takes an argument of type float and performs following computations:
        y=x*2.644
        value of an rgument should be in range of(-inf,2.853] and [88.069, +inf) '''
        try:
            if x > 2.853 and x < 88.069:
                raise ValueError
            y = x*2.644
        except TypeError as error:
            print(f"You got an {error}\nYou need float type")
            y = None
        except ValueError as error:
            print(f"You got Wrong value {error}\n value should be in range of(-inf,2.853] and [88.069, +inf) float type")
            y = None
        return y


if "__main__" == __name__:
	obj = myClass()
	print(myClass.computeFirst(float("1.3")))
	print(myClass.computeSecond(float("1.3")))
	print(myClass.computeThird(float("1.3")))
	print(myClass.computeFourth(float("1.3")))