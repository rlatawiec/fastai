import torch

class KalmanFilter(object):
    def __init__(self):
        ndim, dt = 4, 1.

        self._motion_mat = torch.eye(2 * ndim, 2 * ndim)
        for i in range(ndim):
            self._motion_mat[i, ndim + i] = dt
        self._update_mat = torch.eye(ndim, 2 * ndim)

        self._std_weight_position = 1. / 20
        self._std_weight_velocity = 1. / 160

    def initiate(self, measurement):
        
        mean_pos = measurement
        mean_vel = torch.zeros(mean_pos.size())
        mean = np.r_[mean_pos, mean_vel]
        position = self._std_weight_position * measurement[3]
        velocity = self._std_weight_velocity * measurement[3]
        std = [
            2 * position,
            2 * position,
            1e-2,
            2 * position,
            10 * velocity,
            10 * velocity,
            1e-5,
            10 * velocity]
        covariance = torch.diag(std ** 2)
        return mean, covariance
    
    def predict(self, mean, covariance):
        position_mean = self._std_weight_position * mean[3]
        velocity_mean = self._std_weight_velocity * mean[3]
        std_pos = [position_mean if i else 1e-2 for i in [1, 1, 0, 1]]
        std_vel = [velocity_mean if i else 1e-5 for i in [1, 1, 0, 1]]
        motion_cov = torch.diag(np.r_[std_pos, std_vel] ** 2)
        mean = torch.dot(self._motion_mat, mean)
        covariance = reduce(torch.dot,
                            [self._motion_mat,
                             covariance,
                             self._motion_mat.transpose(1, 0)]) + motion_cov
        return mean, covariance
    
    def project(self, mean, covariance):
        position_mean = self._std_weight_position * mean[3]
        std_pos = [position_mean if i else 1e-1 for i in [1, 1, 0, 1]]
        innovation_cov = torch.diag(std ** 2)
        mean = torch.dot(self._update_mat, mean)
        covariance = reduce(torch.dot,
                            [self._update_mat,
                             covariance,
                             self._update_mat.transpose(1, 0)]) + innovation_cov
        return mean, covariance
    
    def update(self, mean, covariance, measurement):

        projected_mean, projected_cov = self.project(mean, covariance)
        
        cholesky_factorization = projected_cov.cholesky(projected_cov)
        B = torch.dot(covariance, self._update_mat.T).transpose(1, 0)
        kalman_gain = torch.cholesky_solve(B, cholesky_factorization)
        innovation = measurement - projected_mean

        new_mean = mean + torch.dot(innovation, kalman_gain.transpose(1, 0))
        new_covariance = covariance - reduce(torch.dot,
                                             [kalman_gain,
                                              projected_cov,
                                              kalman_gain.transpose(1, 0)])
        return new_mean, new_covariance

