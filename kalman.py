import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class KalmanFilter:
    # Equations found at https://en.wikipedia.org/wiki/Kalman_filter
    def __init__(self, F, B, H, Q, R, x0, P0):
        """
        Initialize the Kalman Filter.

        Args:
            F (ndarray): State transition matrix.
            B (ndarray): Control-input model matrix.
            H (ndarray): Observation model matrix.
            Q (ndarray): Covariance of process noise.
            R (ndarray): Covariance of observation noise.
            x0 (ndarray): Initial state estimate.
            p0 (ndarray): Initial covariance estimate.
        """
        self.F = F  
        self.B = B  
        self.H = H  
        self.Q = Q  
        self.R = R  
        self.x = x0  
        self.P = P0  


    def predict(self, u=None):
        """
        Predict the next state and covariance.

        Args:
            u (ndarray, optional): Control input vector. Default is a zero vector.
        """

        if u is None:
            u = np.zeros((self.B.shape[1], 1))

        # State prediction
        self.x = self.F @ self.x + self.B @ u

        # Covariance prediction
        self.P = self.F @ self.P @ self.F.T + self.Q



    def update(self, z):
        """
        Update the state estimate using the observation.

        Args:
            z (ndarray): Observation vector.

        Returns:
            ndarray: Updated state estimate.
        """



        # Innovation (measurement residual)
        y = z - self.H @ self.x

        # Innovation covariance
        S = self.H @ self.P @ self.H.T + self.R

        # Kalman gain
        K = self.P @ self.H.T @ np.linalg.inv(S)
        # State update
        self.x = self.x + K @ y

        # Covariance update
        self.P = (np.eye(self.P.shape[0]) - K @ self.H) @ self.P



    def get_state(self):
        """
        Return the current state estimate.
        """
        return self.x

    def get_covariance(self):
        """
        Return the current covariance estimate.
        """
        return self.P


class Tracker:
    def __init__(self, steps):
        self.measured_positions = np.zeros((steps, 2))  
        self.estimated_positions = np.zeros((steps, 2))  
        self.positions = np.zeros((steps, 2))  

        self.step_counter = 0 

    def update(self, measured_position, estimated_position, position):
        self.measured_positions[self.step_counter] = measured_position.squeeze()
        self.estimated_positions[self.step_counter] = estimated_position.squeeze()
        self.positions[self.step_counter] = position.squeeze()
        self.step_counter += 1

    def get_trace(self):
        return self.measured_positions, self.estimated_positions, self.positions


if __name__ == "__main__":
    steps = 1000
    F = np.array([[1.0, 0], [0.0, 1.0]])  
    B = np.zeros((2, 1)) 
    H = np.array([[1.0, 0.0], [0.0, 1.0]]) 
    Q = np.eye(2) * 0.005 
    R = np.eye(2) * 0.1
    x0 = np.array([[0], [0]]) 
    P0 = np.eye(2) * 0.001
    kf = KalmanFilter(F, B, H, Q, R, x0, P0)
    tracker = Tracker(steps)
    position = x0
    x_position = position[0][0]
    sigma = 10
    measurment_freq = 100
    for t in range(steps):
        y_position =x_position**2
        
        position = np.array([[x_position], [y_position]]) 
        x_position += 1
        
        kf.predict()
        if t % measurment_freq == 0:
            noise = np.random.randn(*position.shape) * sigma
            measured_position = position + noise
            measured_position = measured_position
            
            kf.update(measured_position)
        estimated_position = kf.get_state()
        tracker.update(measured_position.reshape(1, 2), estimated_position.reshape(1, 2), position.reshape(1, 2))

    measured_positions, estimated_positions, true_positions = tracker.get_trace()
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot true positions (green line)
    true_positions = np.array(true_positions)
    plt.plot(true_positions[:, 0], true_positions[:, 1], label='True Position', color='g', linestyle='-', marker='o')

    # Plot measured positions (red scatter points)
    measured_positions = np.array(measured_positions)
    plt.scatter(measured_positions[:, 0], measured_positions[:, 1], label='Measured Position', color='r', s=10)

    # Plot estimated positions (blue line)
    estimated_positions = np.array(estimated_positions)
    plt.plot(estimated_positions[:, 0], estimated_positions[:, 1], label='Estimated Position', color='b', linestyle='--', marker='x')

    # Labels and title
    plt.legend()
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Kalman Filter: True, Measured, and Estimated Positions')

    # Show the plot
    plt.show()




