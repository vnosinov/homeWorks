
def fun(n, l = [], divisor=1):
    """
    Нахождение делителя с использованием рекурсии
    :param n:
    :param l:
    :param divisor:
    :return:
    """
    if n % divisor == 0:
        l.append(divisor)
    if divisor == n:
        return None
    fun(n, l, divisor+1)
    return l


print(fun(10))

