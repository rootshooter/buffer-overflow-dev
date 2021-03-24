# Work In Progress
This project was tested on a Windows 10 VM running a Vulnserver binary.

Usage: python fuzz.py -t 10.10.10.1 -p 9001 -c "TRUN /.:/"

Usage: python eip_finder.py -t 10.10.10.1 -p 9001 -c "TRUN /.:/"

Usage: python eip_verify.py -t 10.10.10.1 -p 9001 -c "TRUN /.:/" -o 9002

Usage: python bad_char.py -t 10.10.10.1 -p 9001 -c "TRUN /.:/" -o 9002

Usage: python exploit.py -t 10.10.10.1 -p 9001 -c "TRUN /.:/" -o 9002
