from env import GridEnvironment
import time

if __name__ == "__main__":
    env = GridEnvironment()
    state = env.reset()
    print("Initial State:", state)

    done = False
    episode = 1

    while True:
        print(f"Episode {episode}")
        while not done:
            env.render()  # Visualize the environment
            
            # For testing purposes, let's make the robot move randomly:
            action = random.randint(0, 3)  # Random action (Up, Down, Left, Right)
            
            state, reward, done = env.step(action)
            print(f"State: {state}, Reward: {reward}, Done: {done}")
            time.sleep(0.5)  # Wait half a second for visualization

        # Reset the environment after reaching the goal
        print(f"Goal reached in episode {episode}! Resetting...")
        time.sleep(1)  # Short delay before the new episode starts
        state = env.reset()
        done = False
        episode += 1
