# -*- coding: utf-8 -*-

""" netconf_dump.py - Dump xml samples

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

import sys
import snetconf.samples
import xparse.axml
from xparse.enclosed import Enclose

def main():
    run_script(sys.argv[1:])

def run_script(args, verbose=0):
    param = args
    assert not param
    replies = snetconf.samples.replies.infos()["reply"]
    for reply in replies:
        dump_reply(reply, verbose)
        print("==" * 20)

def dump_reply(reply, verbose=0):
    idx, astr = reply
    if verbose > 0:
        shown = " " + astr.strip()
    else:
        shown = ""
    print(f"Reply #{idx}:{shown}")
    ans = xparse.axml.XmlAnswer(astr)
    slist = ans.struct["REP"]
    its = [(elem.memo, elem) for elem in slist]
    print("its:", [memo for memo, _ in its])
    encl = None
    for y_idx, elem in enumerate(slist, 1):
        tree = elem
        encl = Enclose(tree, name=tree.string, subs=tree.own())
        print(f"{y_idx}:", encl)
    return encl

if __name__ == "__main__":
    main()
