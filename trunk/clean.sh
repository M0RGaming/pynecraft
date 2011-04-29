#!/bin/sh

# Directories
rm -rf world

# Files
rm -rf *.txt
rm -rf server*
rm -rf *.log
rm -rf *.pyc
rm -rf *~
rm -rf *.orig
rm -rf *\#

find . -name *~ -exec rm -rf {} \;
find . -name *.pyc -exec rm -rf {} \;
find . -name *\# -exec rm -rf {} \;
find . -name *.orig -exec rm -rf {} \;
