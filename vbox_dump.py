# -*- coding: utf-8 -*-

""" vbox_dump.py - Dump VirtualBox xml

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

import xparse.vbox

DEF_NAME = ""
#DEF_NAME = "bell_SAMPLE.vbox"

def main():
    fname = DEF_NAME if DEF_NAME else "D:/maquinas/vm_vbox/bell/bell.vbox"
    xparse.vbox.main_test(fname)

if __name__ == "__main__":
    main()
