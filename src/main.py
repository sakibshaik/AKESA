#!flask/bin/python
import sys
from pathlib import Path
from webapp.app import mount_web_app

if __package__ is None:
	file = Path(__file__).resolve()
	sys.path.insert(0, str(file.parent.parent))

def main():
	print("called with: ", ', '.join(sys.argv))
	mount_web_app()

if __name__ == '__main__':
    main()