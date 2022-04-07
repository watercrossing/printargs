import sys

print(f"Name of the script      : {sys.argv[0]=}")

print(f"Arguments of the script : {sys.argv[1:]=}")

print("Full command line args  : " + " ".join(sys.argv[1:]))
input("Press enter for exit")