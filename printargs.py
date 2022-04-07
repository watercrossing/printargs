import sys

from pathlib import Path

print(f"Name of the script      : {sys.argv[0]=}")

print(f"Arguments of the script : {sys.argv[1:]=}")

print("Full command line args  : " + " ".join(sys.argv[1:]))

print("Saving arguments to args.log")

with (Path(sys.argv[0]).parent / 'args.log').open('a') as f:
    f.write(" ".join(sys.argv))
    f.write("\n")

input("Press enter to exit")