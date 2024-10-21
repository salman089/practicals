"""pr.9 Title Of Experiment : Implement Reinforcement Learning algorithm."""

# Second file: calculate_utility.py
import numpy as np

# Function to calculate utility using the Bellman equation
def return_state_utility(v, T, u, reward, gamma):
    action_array = np.zeros(4)  # Array to store utility values for each action
    for action in range(4):
        action_array[action] = np.sum(u * np.dot(v, T[:, :, action]))
    return reward + gamma * np.max(action_array)

def main():
    # Starting state vector (1, 1)
    v = np.array([[0.0, 0.0, 0.0, 0.0, 
                   0.0, 0.0, 0.0, 0.0, 
                   1.0, 0.0, 0.0, 0.0]])

    # Load the transition matrix from the saved file
    T = np.load("T.npy")

    # Utility vector for the states
    u = np.array([[0.812, 0.868, 0.918, 1.0,
                   0.762, 0.0, 0.660, -1.0,
                   0.705, 0.655, 0.611, 0.388]])

    # Define the reward for state (1,1)
    reward = -0.4
    gamma = 1.0  # Discount factor

    # Calculate and print the utility of state (1, 1)
    utility_11 = return_state_utility(v, T, u, reward, gamma)
    print("Utility of state (1,1): " + str(utility_11))

# Run the main function
if __name__ == "__main__":
    main()
