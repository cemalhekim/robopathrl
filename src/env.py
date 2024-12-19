import numpy as np
import matplotlib.pyplot as plt

class GridEnvironment:
    def __init__(self, grid_size=(5, 5), start=(0, 0), goal=(4, 4), obstacles=None):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles or [(2, 2), (3, 3)]
        self.reset()

    def reset(self):
        """Resets the environment to the starting state."""
        self.robot_position = self.start
        return self.robot_position

    def step(self, action):
        """Takes an action and updates the robot's position."""
        x, y = self.robot_position

        if action == 0:    # Up
            x -= 1
        elif action == 1:  # Down
            x += 1
        elif action == 2:  # Left
            y -= 1
        elif action == 3:  # Right
            y += 1

        # Check bounds
        if x < 0 or x >= self.grid_size[0] or y < 0 or y >= self.grid_size[1]:
            return self.robot_position, -1, False  # Penalty for hitting walls

        # Check obstacles
        if (x, y) in self.obstacles:
            return self.robot_position, -1, False  # Penalty for hitting obstacles

        # Check goal
        self.robot_position = (x, y)
        if self.robot_position == self.goal:
            return self.robot_position, 10, True  # Reward for reaching the goal

        return self.robot_position, -0.1, False  # Small penalty for each step

    def render(self):
        """Visualizes the grid environment."""
        grid = np.zeros(self.grid_size)
        for obs in self.obstacles:
            grid[obs] = -1
        grid[self.goal] = 2
        grid[self.robot_position] = 1

        plt.imshow(grid, cmap="cool", interpolation="nearest")
        plt.show()
