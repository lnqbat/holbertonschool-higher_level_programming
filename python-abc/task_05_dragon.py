#!/usr/bin/env python3

class SwimMixin:
    """
    Define swimmixn.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Define flymixin.
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Define Dragon.
    """
    def roar(serlf):
        print("The dragon roars!")
