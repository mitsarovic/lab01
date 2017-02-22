#!/usr/bin/env python3.4
import os.path
from mipsTester import runTests

if os.path.isfile("/usr/home/grads/courses/myy402/bin/MarsMYY402_4_5.jar"):
  # This is the path to MarsMYY402_4_5.jar for the lab machines.
  marsJar = "/usr/home/grads/courses/myy402/bin/MarsMYY402_4_5.jar"
else:
  ##########################################
  # This is my set-up for my machine,
  # MODIFY FOR YOUR PERSONAL COMPUTER SETUP!
  #  USING THE FULL PATH TO MarsMYY402_4_5.jar IN YOUR COMPUTER
  ##########################################
  marsJar = "/home/efthym/t/ca_course/MarsMYY402_4_5.jar"

matric = 2941
tests = [ \
 ("Matric simple test",\
  [('^matric:.*$', 'matric: .word %d' %(matric)) ],\
  {'s0' : -1, 's1' : 0x00ff, 's2' : 0x1001002c, 't0' : 0x10010050},\
  {'var1' : matric+1, 0x10010038 : matric+1, 'var2' : 0x1001003c }\
 ) \
]

  
# Change verbose below to True, if you get errors to get more detailed information
print (runTests("../lab01.asm", tests, marsJar, verbose=False))
