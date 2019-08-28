def addn(v,w):
    """
    Argument v: list representing n-vectors
    Argument w: list representing n-vectors
    Return: list representing addition of v and w
    """
    return [ x+y for (x,y) in zip(v,w) ]

def scalar_vector_mult(alpha,v):
    """
    Argument alpha: a scalar 
    Argument v: a list 
    Return: a list of a*v
    """
    return [ alpha*vec for vec in v]
