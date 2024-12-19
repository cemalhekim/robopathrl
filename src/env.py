import numpy as np
import matplotlib.pyplot as plt
import random

class GridEnvironment:
    def __init__(self, grid_size=(25, 25), start=(0, 0), goal=(24, 24), num_obstacles=8):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.num_obstacles = num_obstacles
        self.obstacles = self.generate_obstacles()
        self.reset()

    def generate_obstacles(self):
        """Generate random obstacles in the grid."""
        obstacles = set()
        while len(obstacles) < self.num_obstacles:
            # Randomly place obstacles, ensuring they don't overlap with the start or goal
            x = random.randint(0, self.grid_size[0] - 1)
            y = random.randint(0, self.grid_size[1] - 1)
            if (x, y) != self.start and (x, y) != self.goal:
                obstacles.add((x, y))
        return list(obstacles)

    def reset(self):
        """Reset the environment to the initial state."""
        self.robot_position = self.start
        return self.robot_position

    def step(self, action):
        """Move the robot and return the new state, reward, and if the goal is reached."""
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

        # Move the robot
        self.robot_position = (x, y)

        # Check if the robot reached the goal
        if self.robot_position == self.goal:
            return self.robot_position, 10, True  # Reward for reaching the goal

        return self.robot_position, -0.1, False  # Small penalty for each step

    def render(self):
        """Render the grid and visualize the robot's current state."""
        grid = np.zeros(self.grid_size)
        
        # Mark obstacles
        for obs in self.obstacles:
            grid[obs] = -1
        
        # Mark the goal and the robot's position
        grid[self.goal] = 2
        grid[self.robot_position] = 1

        # Visualize the grid
        plt.imshow(grid, cmap="cool", interpolation="nearest")
        plt.pause(0.1)  # Pause to create an animation effect

