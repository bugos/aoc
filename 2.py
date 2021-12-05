class First():
  moves = {
    'forward': 0,
    'down': 0,
    'up': 0,
  }

  def step(this, direction, distance):
    this.moves[direction] += distance

  def print_res(this):
    print(this.moves['forward'] * (this.moves['down'] - this.moves['up']))

# 2nd
class Second():
  state = {
    'aim': 0,
    'depth': 0,
    'hor_position': 0,
  }

  def step(this, direction, distance):
    if direction == 'up':
      this.state['aim'] -= distance
    if direction == 'down':
      this.state['aim'] += distance
    if direction == 'forward':
      this.state['hor_position'] += distance
      this.state['depth'] += this.state['aim'] * distance
  
  def print_res(this):
    print(this.state['hor_position'] * this.state['depth'])

first = First()
second = Second()
for line in open('2.txt'):
  direction, distance = line.split(' ', 1)
  direction = direction.strip()
  distance = int(distance)

  first.step(direction, distance)
  second.step(direction, distance)

first.print_res()
second.print_res()

