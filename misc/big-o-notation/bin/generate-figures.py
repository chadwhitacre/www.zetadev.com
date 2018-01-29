#!/usr/bin/env python
"""

http://matplotlib.sourceforge.net/

"""
import math
import os
import re
import sys
import traceback

import pylab


# Helpers
# =======

DPI = 72.0
ASPECT_RATIO = 600.0 / 800.0
def size_it(w):
    w_in = w / DPI
    h_in = w_in * ASPECT_RATIO
    return (w_in, h_in)


def commaize(x):
    """Given an int, return a string with commas.
    """
    digits = str(x)
    out = ''
    len_digits = len(digits)
    for i in range(len_digits):
        out += digits[i]
        if (i < len_digits-1) and ((len_digits-1-i)%3 == 0):
            out += ','
    return out


RUNS = float(5) # number of tests to run for each input

def time_it(func, datafunc, **kwargs):
    """Given two functions and some kwargs, return two lists.

        o The kwargs must have keys start, stop, and step, per xrange.

        o The first function is the one we want to test; it must take a single
          argument.

        o The second function takes an integer in xrange(start, stop, step)
          and returns a data object to pass to the first function. We add 1 to
          stop to make it inclusive.

    The return value is two lists of the same length. The first contains the
    integers from xrange; the second contains the time measurements for calling
    the first function with the data from the second function for the int in
    the corresponding position in the first list.

    Actually, in order to smooth out minor variations, we run the test at the
    next level down of granularity for data size and average the results.

    """
    import time

    x = []
    y = []

    start = kwargs.get('start')
    stop = kwargs.get('stop')
    step = kwargs.get('step')

    for i in xrange(start, stop+1, step):

        # Get the data for this test.
        # ===========================

        data = datafunc(i)


        # Perform this test a few times.
        # ==============================

        measurements = []
        for j in xrange(int(RUNS)):
            time_start = time.time()
            func(*data)
            time_end = time.time()

            elapsed = time_end - time_start
            measurements.append(elapsed)


        # Toss out any outliers and average those remaining.
        # ==================================================

        mean = sum(measurements) / RUNS
        deviations_squared = []
        for measurement in measurements:
            deviation = measurement - mean
            deviations_squared.append(deviation * deviation)
        variance = sum(deviations_squared) / RUNS
        stddev = math.sqrt(variance)
        measurements = [val for val in measurements if abs(mean-val) < stddev]
        measurement = sum(measurements) / RUNS


        # Store the results.
        # ==================

        x.append(i)
        y.append(measurement)

    return (x, y)


page_re = re.compile(r'\d\d-.*\.shtml')
pre_re = re.compile(r'<pre>(.*?)</pre>', re.DOTALL)
figure_re = re.compile(r'<!--figure *(\S*)[ ]*\n(.*?)\n-->', re.DOTALL)
def main(filename_only, figname_only):
    for filename in sorted(os.listdir('.')):
        if filename_only:
            if (filename != filename_only):
                continue
        elif (filename != 'index.shtml') and not page_re.match(filename):
            continue

        word = 'figures' if not figname_only else figname_only
        print "processing %s in %s" % (word, filename)
        raw = open(filename).read().strip()
        pycode = pre_re.search(raw)
        if pycode is not None:
            i = 1
            for figname, figure in figure_re.findall(raw):
                if figname_only and (figname != figname_only):
                    continue
                ns = dict()
                ns['time_it'] = time_it
                ns['commaize'] = commaize
                exec 'from pylab import *' in ns
                try:
                    pylab.clf()
                    pylab.figure(figsize=(size_it(500)))
                    exec pycode.group(1) in ns
                    sys.stdout.write('  %s => ' % figname);
                    sys.stdout.flush()
                    exec figure in ns
                    imgname = '%s.%s.png' % (filename[:-6], figname)
                    pylab.savefig(os.path.join('img', imgname), dpi=DPI)
                    print imgname
                except:
                    print
                    m = "Problem with figure #%d in %s" % (i, filename)
                    print m
                    print '-'*len(m)
                    traceback.print_exc()
                    print
                i += 1


if __name__ == '__main__':
    filename = figname = ''
    nargs = len(sys.argv)
    if nargs == 3:
        filename, figname = sys.argv[1:3]
    elif nargs == 2:
        filename = sys.argv[1]
    elif nargs == 1:
        filename = figname = None
    else:
        print >> sys.stderr, "this script takes 0, 1, or 2 arguments"
        raise SystemExit

    main(filename, figname)
