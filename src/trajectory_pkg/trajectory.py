import math

class TrajectoryValues:
    def __init__(self, x, y, dx, dy, ddx, ddy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = ddx
        self.ddy = ddy

class CommandValues:
    def __init__(self, linear, angular):
        self.linear = linear
        self.angular = angular

class FigureEight:
    def __init__(self, width, height, period):
        self.W = width
        self.H = height
        self.T = period
    
    def find_trajectory(self, t):
        print("finding trajectory...")

        x = (self.W / 2) * math.sin((2 * math.pi * t) / (self.T))
        y = (self.H / 2) * math.sin((4 * math.pi * t) / (self.T))

        print("x is ", x, "y is ", y)
        
        dx = ((self.W * math.pi) / self.T) * math.cos((2 * math.pi * t) / (self.T))
        dy = ((2 * self.H * math.pi) / self.T) * math.cos((4 * math.pi * t) / (self.T))

        print("dx is ", dx, "dy is ", dy)

        ddx = -((2 * self.W * math.pi**2) / (self.T**2)) * math.sin((2 * math.pi * t) / (self.T))
        ddy = -((8 * self.H * math.pi**2) / (self.T**2)) * math.sin((4 * math.pi * t) / (self.T))

        print("ddx is ", ddx, "ddy is ", ddy)

        print("found trajectory!!")
        return TrajectoryValues(x, y, dx, dy, ddx, ddy)


def calculate_control(trajectory_vals):

    print("calculating velocity commands...")

    dx = trajectory_vals.dx
    dy = trajectory_vals.dy
    ddx = trajectory_vals.ddx
    ddy = trajectory_vals.ddy

    v = math.sqrt(dx**2 + dy**2)
    w = (ddy * dx - ddx * dy) / (dy**2 + dx**2)

    print("calculated velocity commands!!")
    return CommandValues(v, w)