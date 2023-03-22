from math import sqrt

class Stats:

    def standardError(self, x):
        ## RETURNS
        # standard error - population
        # standard error - sample
        N = len(x)
        std_population, std_sample = self.standardDeviation(x=x)
        return (std_population/sqrt(N)), (std_sample/sqrt(N))

    def standardDeviation(self, x):
        ## RETURNS
        # standard deviation - population
        # standard deviation - sample
        x_variance_population, x_variance_sample = self.variance(x=x)
        return sqrt(x_variance_population), sqrt(x_variance_sample)

    def variance(self,x):
        ## RETURNS:
        # variance - population
        # variance - sample
        N = len(x)
        total_residual_squared = 0
        x_avg = self.average(x=x)
        for i in x:
            total_residual_squared += ((self.residual(x_i=i,x_avg=x_avg))**2)
        return ((total_residual_squared/N), (total_residual_squared/(N-1)))

    def residual(self,x_i,x_avg):
        return (x_i - x_avg)

    def average(self,x):
        N = len(x)
        x_total = 0
        for i in x:
            x_total += i
        return (x_total/N)
