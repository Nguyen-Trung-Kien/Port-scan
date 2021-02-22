import socket
from IPy import IP

def scan(target):
	convert_ip = checkip(target)
	print('\n' + '[-_0 Scanning Target :]' + str(target))
	for port in range(1,500):
		scan_port(convert_ip,port)
def checkip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)
def get_banner(s):
	return s.recv(1024)
def scan_port(ipadderss, port):
	try:
		sock = socket.socket()
		sock.settimeout(0.05)
		sock.connect((ipadderss, port))
		try:
			banner = get_banner(sock)
			print('[+] Port Open ' + str(port) +' : ' + str(banner.decode().strip('\n')))
		except:
			print('[+] Port Open ' + str(port))
		
	except:
		pass


#convert_ip = checkip(ipadderss)
#port_num = input('Enter Number of port u want to scan:')
if __name__ == "__main__":
	targets = input('[+] Enter target To Scan: ')

	if ',' in targets:
		for ip_add in targets.split(','):
			scan(ip_add.strip(' '))
	else:
		scan(targets)
