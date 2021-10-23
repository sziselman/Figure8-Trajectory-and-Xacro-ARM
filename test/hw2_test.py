import unittest
from trajectory_pkg.trajectory import FigureEight, calculate_control

class TestCase(unittest.TestCase):
    
    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")

    def test_trajectory_and_command_time0(self):
        # initializing a figure eight of width 5, height 8, period 10
        fig_eight = FigureEight(5, 8, 10)
        # finding the trajectory values at time t = 0.0
        vals = fig_eight.find_trajectory(0.0)
        # calculate command values to maintain trajectory
        cmds = calculate_control(vals)

        self.assertAlmostEquals(vals.x, 0.0)
        self.assertAlmostEquals(vals.y, 0.0)

        self.assertAlmostEquals(vals.dx, 1.570796327)
        self.assertAlmostEquals(vals.dy, 5.026548246)

        self.assertAlmostEquals(vals.ddx, 0.0)
        self.assertAlmostEquals(vals.ddy, 0.0)

        self.assertAlmostEquals(cmds.linear, 5.266268923)
        self.assertAlmostEquals(cmds.angular, 0.0)

    def test_trajectory_and_command_time5(self):
        # initiailizing a figure eight of width 5, height 8, period 10
        fig_eight = FigureEight(5, 8, 10)
        # finding the trajectory values at time t = 0.0
        vals = fig_eight.find_trajectory(5.0)
        # calculate command values to maintain trajectory
        cmds = calculate_control(vals)

        self.assertAlmostEquals(vals.x, 0.0)
        self.assertAlmostEquals(vals.y, 0.0)

        self.assertAlmostEquals(vals.dx, -1.570796327)
        self.assertAlmostEquals(vals.dy, 5.026548246)

        self.assertAlmostEquals(vals.ddx, 0.0)
        self.assertAlmostEquals(vals.ddy, 0.0)

        self.assertAlmostEquals(cmds.linear, 5.266268923)
        self.assertAlmostEquals(cmds.angular, 0.0)


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun('homework2', 'test_homework2', TestCase)