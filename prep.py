#import MySQLdb as mdb
import os.path

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2014 Paul Matthews <paulus@paulus-laptop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



def main():
   indirname = "/home/paulus/docs/datalit/"
   #outdirname = "/home/paulus/docs/kobo-html/"
    
   for fn in os.listdir(indirname ):
       if fn.endswith(".pdf"):
          print "converting - " + fn

          cmd = "pdftotext  '" + indirname + fn + "' '" + indirname + fn +  ".txt'"    
          print os.system(cmd)


if __name__ == '__main__':
	main()

