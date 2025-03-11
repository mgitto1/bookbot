from stats import print_report
import sys

def main():
  if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    exit(1)
  else:
    print_report(sys.argv[1])
  pass

main()
