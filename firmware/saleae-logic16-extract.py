#!/usr/bin/python3
##
## This file is part of the sigrok-util project.
##
## Copyright (C) 2013 Marcus Comstedt <marcus@mc.pp.se>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

import sys
import parseelf

def extract_symbol(elf, symname, filename):
    blob = elf.load_symbol(elf.dynsym[symname])
    f = open(filename, 'wb')
    f.write(blob)
    f.close()
    print("saved %d bytes to %s" % (len(blob), filename))

def extract_bitstream(elf, lv):
    extract_symbol(elf, 'gLogic16Lv'+lv+'CompressedBitstream',
                   'saleae-logic16-fpga-'+lv+'.bitstream')

def usage():
    print("saleae-logic16-extract.py <programfile>")
    sys.exit()


#
# main
#

if len(sys.argv) != 2:
    usage()

try:
    filename = sys.argv[1]
    elf = parseelf.elf(filename)
    extract_bitstream(elf, '18')
    extract_bitstream(elf, '33')
except Exception as e:
    print("Error: %s" % str(e))

