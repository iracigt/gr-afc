#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr

class fsk_afc_ff(gr.sync_block):
    """
    docstring for block fsk_afc_ff
    """
    def __init__(self, ntaps):
        self.max_buf = numpy.zeros((ntaps,), dtype=numpy.float32)
        self.min_buf = numpy.zeros((ntaps,), dtype=numpy.float32)
        self.samp_buf = numpy.zeros((3,), dtype=numpy.float32)
        self.min = 0
        self.max = 0
        gr.sync_block.__init__(self,
            name="fsk_afc_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(0, len(in0)):
            self.samp_buf[1:] = self.samp_buf[:-1]
            self.samp_buf[0] = in0[i]

            if self.samp_buf[0] <= self.samp_buf[1] and self.samp_buf[1] > self.samp_buf[2] and self.samp_buf[1] > 0:
                self.max_buf[1:] = self.max_buf[:-1]
                self.max_buf[0] = self.samp_buf[1]
                self.max = sum(self.max_buf) / float(len(self.max_buf))

            if self.samp_buf[0] >= self.samp_buf[1] and self.samp_buf[1] < self.samp_buf[2] and self.samp_buf[1] < 0:
                self.min_buf[1:] = self.min_buf[:-1]
                self.min_buf[0] = self.samp_buf[1]
                self.min = sum(self.min_buf) / float(len(self.min_buf))

            in0[i] = in0[i] - (self.max + self.min)/2.0

        out[:] = in0
        return len(output_items[0])
