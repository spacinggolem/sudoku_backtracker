class Cell():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

    def is_empty(self):
        if self.num == 0:
            return True
        return False