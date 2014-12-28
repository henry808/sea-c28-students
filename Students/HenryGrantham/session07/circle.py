#!/usr/bin/env python
"""circle class --
fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self._diameter = radius * 2.0
        self._area = math.pi * self.radius ** 2.0

    # unbound method
    @staticmethod
    def from_diameter(diameter):
        return Circle(diameter / 2.0)

    def _getdiameter(self):
        return self._diameter

    def _setdiameter(self, di):
        self._diameter = di
        self.radius = di / 2.0
        self._area = math.pi * self.radius ** 2.0

    def _deldiameter(self):
        del self._diameter

    diameter = property(_getdiameter, _setdiameter, _deldiameter)

    def _setarea(self, area):
        raise AttributeError

    def _getarea(self):
        return self._area

    def _delarea(self):
        del self._area

    area = property(_getarea, _setarea, _delarea)

    def __str__(self):
        return "Circle with radius: {:f}".format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, circle2):
        return Circle(self.radius + circle2.radius)

    def __mul__(self, multiple):
        return Circle(self.radius * multiple)

    def __eq__(self, circle2):
        return self.radius == circle2.radius

    def __le__(self, circle2):
        return self.radius <= circle2.radius

    def __ge__(self, circle2):
        return self.radius >= circle2.radius

    def __lt__(self, circle2):
        return self.radius < circle2.radius

    def __gt__(self, circle2):
        return self.radius > circle2.radius
