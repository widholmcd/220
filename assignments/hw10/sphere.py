"""
Name: Calvin Widholm
sphere.py

Problem: creating methods for a sphere class

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from math import pi

class Sphere:
    """
    sphere constructor here
    """
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        surface_area = 4 * pi * (self.radius ** 2)
        return float(surface_area)

    def volume(self):
        volume = (4 / 3) * pi * (self.radius ** 3)
        return float(volume)
