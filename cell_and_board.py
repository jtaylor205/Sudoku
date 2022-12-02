class Cell:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
    def get_value(self):
        return self.value
    def get_pos(self):
        return self.pos

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value