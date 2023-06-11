import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    #contents should be a list of strings containing one item for each ball in the hat.
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    print(self.contents)

  def draw(self, number):
    balls_removed = []
    #If the number of balls to draw exceeds the available quantity, return all the balls.
    if(number > len(self.contents)):
      return self.contents
      #The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. 
    for i in range(number):
      removed = self.contents.pop(int(random.choice(range(len(self.contents)))))
      balls_removed.append(removed)
    return balls_removed
  

#program to determine the approximate probability of drawing certain balls randomly from a hat.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)

    for color in colors_gotten:
      if(color in expected_copy):
        expected_copy[color]-=1

    if(all(x <= 0 for x in expected_copy.values())):
      count +=1

  return count / num_experiments