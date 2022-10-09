# -*- coding: utf-8 -*-

""" vbox_dump.py - Dump VirtualBox xml

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

import enclose
import xparse.vbox
from xparse.elems import SElem

DEF_NAME = ""
#DEF_NAME = "bell_SAMPLE.vbox"

def main():
    fname = DEF_NAME if DEF_NAME else "D:/maquinas/vm_vbox/bell/bell.vbox"
    vbx = xparse.vbox.main_test(fname)
    tree = SElem(vbx.own())
    encl = enclose.Enclose(tree, name=tree.string, subs=tree.own())
    encl.parse()
    print("==" * 20)
    astr = encl.get_data()
    print(astr)
    print("==" * 20)

if __name__ == "__main__":
    main()
