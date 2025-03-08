from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Create the Super Mario Bros. environment with compatibility flags
env = gym_super_mario_bros.make('SuperMarioBros-v3', apply_api_compatibility=True, render_mode='human')
env = JoypadSpace(env, SIMPLE_MOVEMENT)  # Simplify the action space

# Initialize done flag
done = True

# Main loop
for step in range(5000):  # Run for 5000 steps
    if done:
        # Handle reset based on API version
        reset_result = env.reset()
        if isinstance(reset_result, tuple):
            state, info = reset_result  # New API: (obs, info)
        else:
            state = reset_result  # Old API: just obs
            info = {}

    # Take a random action and handle step based on API version
    step_result = env.step(env.action_space.sample())
    if len(step_result) == 5:
        state, reward, terminated, truncated, info = step_result  # New API
        done = terminated or truncated  # Combine for old-style done
    else:
        state, reward, done, info = step_result  # Old API

    env.render()  # Display the game window

env.close()  # Close the environment