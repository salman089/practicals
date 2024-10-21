"""pr.9 Title Of Experiment : Implement Reinforcement Learning algorithm."""


# First file: create_transition_matrix.py
import numpy as np

# Create a transition matrix T with dimensions (states x next_states x actions)
# Here, we have 12 states and 4 possible actions
T = np.zeros((12, 12, 4))

# Generate random transition probabilities
for action in range(4):  # For each action (0 to 3)
    for s1 in range(12):  # For each current state (s1)
        # Assign probabilities to next states (s2) for this action
        for s2 in range(12):
            if s1 != s2:  # Avoid self-loops
                T[s1, s2, action] = np.random.random()  # Random probability

        # Normalize to ensure probabilities sum to 1
        T[s1, :, action] /= np.sum(T[s1, :, action])

# Save the transition matrix to a file
np.save("T.npy", T)
