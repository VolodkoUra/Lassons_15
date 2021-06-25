class MyClass:
    def __init__(self, k):
        self.k = k

    def decoration_except(foo):
        def wrapper(*args, **kwargs):

            try:
                result = foo(*args, **kwargs)
                return result
            except ZeroDivisionError:
                print("На ноль делить нельзя")
                return 0
            except Exception as ex:
                print(ex)
        return wrapper

    def decoration_log(foo):
        def wrapper(*args, **kwargs):
            g = foo(*args, **kwargs)
            result = next(g)
            with open("text.log", "a") as file:
                file.write(str(result) + "\n")
            return result
        return wrapper

    def fuct(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n* self.fuct(n - 1)


    @decoration_except
    @decoration_log
    def power_c(self):
        result = 0
        p = 0
        while p <= self.k:
            res = 4 * p
            result += (self.fuct(res) / self.fuct(p) ** 4) * (1103 + 26390 * p)/(4*99)**(4*p)
            p += 1
            pi = 9801/((2*2**(1/2)) * result)
            yield pi

