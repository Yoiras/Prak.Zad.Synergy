class BaseClass:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        return f"Базовый класс: {self.name}"
    
    def calculate(self, x):
        return x * 2


class DerivedClass(BaseClass):
    def __init__(self, name, version):
        super().__init__(name)
        self.version = version
    
    def display_info(self):
        return f"{super().display_info()}\nПроизводный класс, версия: {self.version}"
    
    def calculate(self, x):
        base = super().calculate(x)
        return base + x * 3


# Демонстрация
base = BaseClass("BaseObj")
derived = DerivedClass("DerivedObj", "2.1")

print(base.display_info())
print("calculate(5) =", base.calculate(5))
print("\n" + derived.display_info())
print("calculate(5) =", derived.calculate(5))
