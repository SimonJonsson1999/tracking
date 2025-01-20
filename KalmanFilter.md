# Kalman Filter Overview

The **Kalman Filter** is a mathematical method that allows for estimation of a state from noisy measurements. This is interesting in this project because a detection model could give false detections or the objcet could be occluded. The Kalman Filter wil be able to estimate a position even if a measurement (detection) is unavailable.

# Kalman Filter Basics
Some basics to understand and be able to tune a Kalman Filter
## Model
The Kalman Filter model assumes the state $x_k$ evolves according to the following equation
$$x_k = F_kx_{k-1} + B_ku_k + w_k$$
Where:

- $x_k$ is the state vector at time step k .
- $F_k$ is the state transition matrix, which models how the state evolves from time k-1 to time k.
- $B_k$ is the control input matrix, which models the influence of the control input u_k on the system at time k.
- $u_k$ is the control input at time k, which can be used to apply external forces or actions to the system.
- $w_k$ is the process noise, which represents random disturbances affecting the state evolution, assumed to be Gaussian with zero mean and covariance $Q_k$.

In addition to the state evolution equation, the Kalman Filter also assumes that the observations or measurements $z_k$ at each time step k are related to the state through the following equation:

$$
z_k = H_k x_k + v_k
$$


Where:

- $z_k$ is the measurement vector at time k.
- $H_k$ is the measurement matrix that maps the state vector $x_k$ to the measurement space.
- $v_k$ is the measurement noise, assumed to be Gaussian with zero mean and covariance $R_k$.

## Details
The Kalman filter is a recursive estimator, meaning that the previous estimated state is the starting point of the new estimated state.

The estimations are divided into 2 stages, a predict and an update.

### Predict

In the **Prediction** stage, the Kalman Filter predicts the state at the next time step, based on the previous state and control inputs. The key equations in this stage are:

1. **State Prediction**:
   $$ 
   \hat{x}_{k|k-1} = F_k \hat{x}_{k-1|k-1} + B_k u_k
   $$

   Where:
   - \( \hat{x}_{k|k-1} \) is the predicted state estimate at time \( k \).
   - \( F_k \) is the state transition matrix, which describes how the system evolves over time.
   - \( \hat{x}_{k-1|k-1} \) is the state estimate from the previous time step \( k-1 \).
   - \( B_k \) is the control input matrix, and \( u_k \) is the control vector, representing the influence of any external inputs on the system.

2. **Error Covariance Prediction**:
   $$
   P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q_k
   $$

   Where:
   - \( P_{k|k-1} \) is the predicted error covariance.
   - \( P_{k-1|k-1} \) is the error covariance from the previous time step.
   - \( Q_k \) is the process noise covariance, representing uncertainty in the prediction due to random disturbances.

The **Prediction** stage produces two outputs:
- **Predicted state estimate**: \( \hat{x}_{k|k-1} \).
- **Predicted error covariance**: \( P_{k|k-1} \).

These provide the best estimate of the state before receiving the new measurement.

### Update

In the **Update** stage, the Kalman Filter refines the predicted state based on the new measurement \( z_k \). This stage adjusts the predicted state estimate by correcting it with the measurement, considering the measurement noise.

1. **Compute the Kalman Gain**:
   $$
   K_k = P_{k|k-1} H_k^T (H_k P_{k|k-1} H_k^T + R_k)^{-1}
   $$

   Where:
   - $K_k$ is the Kalman gain, which determines how much weight should be given to the new measurement relative to the predicted state.
   - $P_{k|k-1}$ is the predicted error covariance.
   - $H_k$ is the measurement matrix, which maps the state to the measurement space.
   - $R_k$ is the measurement noise covariance.

2. **State Update**:
   $$
   \hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (z_k - H_k \hat{x}_{k|k-1})
   $$

   Where:
   - $\hat{x}_{k|k}$ is the updated state estimate at time k.
   - $z_k$ is the measurement at time k.
   - $H_k \hat{x}_{k|k-1}$ is the predicted measurement based on the predicted state.
   - $z_k - H_k \hat{x}_{k|k-1}$ is the residual or innovation, which represents the difference between the actual and predicted measurements.

3. **Error Covariance Update**:
   $$
   P_{k|k} = (I - K_k H_k) P_{k|k-1}
   $$

   Where:
   - \( P_{k|k} \) is the updated error covariance.
   - \( I \) is the identity matrix, ensuring that the update equation works for all dimensions of the state vector.

The **Update** stage produces the following outputs:
- **Updated state estimate**: \( \hat{x}_{k|k} \).
- **Updated error covariance**: \( P_{k|k} \).

The updated state is now the best estimate of the system's state, taking into account both the prediction and the new measurement.

---

