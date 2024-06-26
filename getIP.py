import socket
import sys
import argparse

parser = argparse.ArgumentParser(description="Get Ip of Websites",
                                 usage='%(prog)s -u/--url ',
                                 epilog=f"python {sys.argv[0]} -u www.example.com")

parser.add_argument("--url", '-u',
                    help="takes website URL",
                    required=True,
                    dest="link")
print('''              
 
░██████╗░███████╗████████╗██╗██████╗░
██╔════╝░██╔════╝╚══██╔══╝██║██╔══██╗
██║░░██╗░█████╗░░░░░██║░░░██║██████╔╝
██║░░╚██╗██╔══╝░░░░░██║░░░██║██╔═══╝░
╚██████╔╝███████╗░░░██║░░░██║██║░░░░░
░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░ \nsrimant\n\n''')
# if user doesn't give any argument
args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit()

url = args.link

def get_IP():
    host_name = str(url)
    try:
        print(f"IP address of {host_name}:"
              f"{socket.gethostbyname(host_name)}")
    except socket.error as err_msg:
        print(f"{url},{err_msg}")
if __name__ == '__main__':
    get_IP()