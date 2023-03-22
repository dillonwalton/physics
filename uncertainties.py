class Uncertainties:
    
    def chiSquare(self, data, theory):
        j=1538
        final_sum = 0
        for i in theory:
            final_sum += (((data[j] - theory[j])**2)/(theory[j]))
            j+=1
        return(final_sum/(j-1538))