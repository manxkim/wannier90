"""
Parser function parse() for a real-space Cartesian tensor operator file.
"""
from __future__ import print_function, unicode_literals
import inspect
from collections import defaultdict

from . import show_output


def parse(fname):
    """Parse a tensor-R file with nine complex Cartesian components."""
    retdict = defaultdict(list)
    labels = ('xx', 'xy', 'xz', 'yx', 'yy', 'yz', 'zx', 'zy', 'zz')

    if show_output:
        print("[{}.{}] Parsing file '{}'".format(
            __name__, inspect.currentframe().f_code.co_name, fname))

    with open(fname) as f:
        lines = f.readlines()

    retdict['num_wann'] = [int(value) for value in lines[1].split()]
    retdict['nrpts'] = [int(value) for value in lines[2].split()]

    for line in lines[3:]:
        pieces = line.split()
        if len(pieces) != 23:
            raise ValueError("Wrong line length ({}, instead of 23); line content: {}".format(
                len(pieces), line))
        retdict['irvec_a'].append(int(pieces[0]))
        retdict['irvec_b'].append(int(pieces[1]))
        retdict['irvec_c'].append(int(pieces[2]))
        retdict['index_i'].append(int(pieces[3]))
        retdict['index_j'].append(int(pieces[4]))
        for component, label in enumerate(labels):
            retdict['real_{}'.format(label)].append(float(pieces[5 + 2*component]))
            retdict['imag_{}'.format(label)].append(float(pieces[6 + 2*component]))

    retdict = dict(retdict)
    if show_output:
        for key in sorted(retdict):
            print("  {}: {}".format(key, retdict[key]))
        print("-"*72)
    return retdict
