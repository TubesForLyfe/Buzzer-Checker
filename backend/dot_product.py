def Length(vector):
    return (vector[0]**2 + vector[1]**2 + vector[2]**2)**0.5

def CosineSimilarity(vector1, vector2):
    return (vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]) / (Length(vector1) * Length(vector2))