""" A design pattern that ensures that a class can only  have one instance """


class Singleton:
    """ Singleton class that allows only one instance to be instantiated"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    # The client code.

    s1 = Singleton()
    print('s1 = ', s1)
    s1 = Singleton()
    print('s1 = ', s1)
    s2 = Singleton()
    print('s2 = ', s2)

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print('The Singleton worked, s1 = s2.')
        print('s1 = ', s1)
        print('s2 = ', s2)
    else:
        print('The Singleton did not work, s1 != s2.')
        print('s1 = ', s1)
        print('s2 = ', s2)
