class VectorXY:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def __add__(self, other):
    return VectorXY(self.x + other.x, self.y + other.y)


def __mul__(self, arg):
    if arg.__class__.__name__ == 'int':
        return VectorXY(self.x * arg, self.y * arg)
    if arg.__class__.__name__ == 'VectorXY':
        return (self.x * arg.x) + (self.y * arg.y)
    else:
        return None
