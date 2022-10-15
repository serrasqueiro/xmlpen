# -*- coding: utf-8 -*-

""" vbox_dump.py - Dump VirtualBox xml

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

import sys
import xparse.vbox
from xparse.enclosed import Enclose
from xparse.elems import SElem

DEF_NAME = "bell_SAMPLE.vbox"

def main():
    run_script(sys.argv[1:])

def run_script(args):
    param = args if args else [DEF_NAME]
    fname = param[0]
    if len(param) > 1:
        print("Ignored extra params:", param[1:])
    vbx = xparse.vbox.main_test(fname)
    tree = SElem(vbx.own())
    encl = Enclose(tree, name=tree.string, subs=tree.own())
    encl.parse()
    print("==" * 20)
    astr = encl.get_data()
    print(astr)
    print("==" * 20)

if __name__ == "__main__":
    main()
