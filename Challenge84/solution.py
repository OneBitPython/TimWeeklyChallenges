class checkIsNumber():
    def __init__(self, val):
        self.val = val
        self.digits = "0123456789"
    def mhmadidas(self):
        return self.val in self.digits
class required():
    def __init__(self, value):
        self.__value = value
    
    @property
    def value(self):
        return self.__value
class instantiate():
    def instantiate_reee():
        return ""
class getTheGoddamnInput():
    def inputgetteruseless():
        return input()


T = getTheGoddamnInput.inputgetteruseless()
for q in range(int(T)):
    val = getTheGoddamnInput.inputgetteruseless()
    final = instantiate.instantiate_reee()

    if isinstance(val, int):
        print("lmao")
    else:
        for value in val:
            number = checkIsNumber(value)
            if number.mhmadidas():
                pass
                #noob lmao
            else:
                not_number = required(value)
                final = final+not_number.value
        print(final)
#yes, I had time to kill mhmadidas