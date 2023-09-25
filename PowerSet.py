def powerset(inputSet):
    
    output = []
    n = len(inputSet)
    
    def powersetBacktrack(subset, start):
        output.append(subset[:])
        
        for i in range(start, n):
            subset.append(inputSet[i])
            
            powersetBacktrack(subset, i+1)
            
            subset.pop()
            
    powersetBacktrack([], 0)
    
    return output
