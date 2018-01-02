from contract import Base, PositiveInteger

dx: PositiveInteger

class Player(Base):
    name: NonEmptyString
    x: Integer
    y: Integer

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx

p = Player('아드', 0, 0)
p.left(-1)
