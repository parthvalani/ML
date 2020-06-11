import numpy as np   
class LinearRegressionUsingGD: 
    #Linear Regression Using Gradient Descent.  
    def __init__(self, eta=0.05, n_iterations=1000): 
        self.eta = eta 
        self.n_iterations = n_iterations  
    def fit(self, x, y): 
        #Fit the training data  
        self.cost_ = [] 
        self.w_ = np.zeros((x.shape[1], 1)) 
        m = x.shape[0]  
        for _ in range(self.n_iterations): 
            y_pred = np.dot(x, self.w_) 
            residuals = y_pred - y 
            gradient_vector = np.dot(x.T, residuals) 
            self.w_ -= (self.eta / m) * gradient_vector 
            cost = np.sum((residuals ** 2)) / (2 * m) 
            self.cost_.append(cost) 
        return self  
    def predict(self, x): 
        # Predicts the value  
        return np.dot(x, self.w_) 