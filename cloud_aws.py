import boto3

if __name__ == '__main__':
	number = 0
	while True:
		print("                                                            ")
		print("                                                            ")
		print("------------------------------------------------------------")
		print("           Amazon AWS Control Panel using SDK               ")
		print("                                                            ")
		print("  Cloud Computing, Computer Science Department              ")
		print("                           at Chungbuk National University  ")
		print("------------------------------------------------------------")
		print("  1. list instance                2. available zones        ")
		print("  3. start instance               4. available regions      ")
		print("  5. stop instance                6. create instance        ")
		print("  7. reboot instance              8. list images            ")
		print("                                 99. quit                   ")
		print("------------------------------------------------------------")
		number = int(input("Enter an integer:"))
