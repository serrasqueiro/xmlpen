# -*- coding: utf-8 -*-

""" netconf_dump.py - Dump xml samples

Author: Henrique Moreira, h@serrasqueiro.com
"""

# pylint: disable=missing-function-docstring

import sys
import mgx
import snetconf.samples
import xparse.axml
from xparse.enclosed import Enclose

def main():
    run_script(sys.argv[1:])

def run_script(args, verbose=0):
    param = args
    assert not param
    replies = snetconf.samples.replies.infos()["reply"]
    res = wrapped_replies(replies, verbose)
    assert res

def wrapped_replies(replies, verbose=0) -> list:
    """ Returns the list of enclosed replies. """
    alists = []
    for reply in replies:
        idx, astr = reply
        assert idx >= 0, f"wrong idx={idx}"
        if idx <= 0:
            continue
        assert astr, f"bad str at idx={idx}"
        alist = dump_reply(reply, verbose)
        elist = [encl for _, encl in alist]
        if elist:
            wrap = mgx.envelope.Envelope(elist, elist[-1]["string"])
            wrap.dump()
        print("==" * 20)
        alists.append(alist)
    return alists

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
    res = []
    for y_idx, elem in enumerate(slist, 1):
        tree = elem
        encl = Enclose(tree, name=tree.string, subs=tree.own())
        print(f"{y_idx}:", encl)
        res.append((y_idx, encl))
    return res

if __name__ == "__main__":
    main()
