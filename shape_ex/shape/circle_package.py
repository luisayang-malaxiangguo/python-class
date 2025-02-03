import math

class Circle:
    def __init__(self, centre, radius):
        """Initialize a circle with a centre (tuple of length 2) and radius (float)."""
        if len(centre) != 2:
            raise ValueError("Centre must be a 2D coordinate (tuple of length 2)")
        if radius <= 0:
            raise ValueError("Radius must be positive")

        self.centre = tuple(centre)
        self.radius = radius

    def __contains__(self, point):
        """Check if a given point (tuple) is inside the circle."""
        if len(point) != 2:
            raise ValueError("Point must be a 2D coordinate (tuple of length 2)")
        
        # Calculate Euclidean distance
        distance = math.sqrt((point[0] - self.centre[0])**2 + (point[1] - self.centre[1])**2)
        
        return distance <= self.radius
