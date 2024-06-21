from gbEnvironment.PyBoyWrapper import PyBoyWrapper
import sys

maxActions = 100000
assert(len(sys.argv) >= 2)

rom = sys.argv[1]
pyboy = PyBoyWrapper(rom, maxActions)
