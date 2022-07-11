import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Setting the constants allow you to make game changes without digging through the entire code
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
class Snake:

    def __init__(self):
        self.snake = [] #eventually becomes a list of Turtles
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.setpos(position)
        self.snake.append(new_segment) #appends Turtles into the list self.snake

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1): #start is larger than stop in range(), making the for loop iterate in descending order
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE) #moves the head segment forward by MOVE_DISTANCE

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def turn_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def reset(self):
        for segment in self.snake:
            segment.goto(x=1000,y=1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

