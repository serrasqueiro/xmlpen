# -*- coding: utf-8 -*-

""" enclose.py - enclose SElem trees

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

class XDict(dict):
    """ Generic dictionary """
    def __init__(self, *args, **kwargs):
        name = kwargs.pop('name', '')
        self._name = name
        there = args[0]
        rest = args[1:]
        assert not rest
        dict.__init__(self, rest, **kwargs)
        self._data = {"tree": there}

    def named(self) -> str:
        return self._name

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

class Enclose(XDict):
    """ Enclose elements of a tree
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state = "A"
        self._fab = {}

    def get_data(self):
        return self._data if self._state == "A" else self._fab

    def parse(self):
        """ Parses SElem contents """
        # dct = {k: fun(v) for k, v in self.items()}
        # or
        # dct = dict(map(lambda item: (item[0], fun(item[1])), self.items()))
        if self._state != "A":
            return False
        tree = self._data["tree"]
        within = {
            "attrib": tree.own().attrib,
            "data": tree.subs(),
        }
        self._fab = {
            tree.string: within,
        }
        self._state = "B"
        return True

def fun(item):
    return item + "!"
