class Win_Door:
  def __init__(self, w, h):
    self.square = w * h 

class Room:
  def __init__(self, l, w, h):
    self.length = l
    self.width = w
    self.height = h
    self.wd = []

  def addWD(self, w, h):
    self.wd.append(Win_Door(w, h))

  def fullSerface(self):
    return 2 * self.height * (self.length + self.width)

  def workSurface(self):
    new_square = self.fullSerface()
    for i in self.wd:
      new_square -= i.square
    return new_square

  def wallpapers(self, d, s):
    return  int(self.workSurface() / (d * s))
