import boto3
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')

### list_instance 함수
def list_instance() :
	instance_ids = []
	number = 1
	response = client.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])
	instances_full_details = response['Reservations']
	for instance_detail in instances_full_details:
        	group_instances = instance_detail['Instances']

        	for instance in group_instances:
            		instance_id = instance['InstanceId']
            		instance_ids.append("[id] " + instance_id)
            		image_id = instance['ImageId']
            		instance_ids.append("[AMI] " + image_id)
            		instance_type = instance['InstanceType']
            		instance_ids.append("[type] " + instance_type)
            		instance_state = instance['State']
            		instance_ids.append("[state] " + instance_state['Name'])
            		instance_monitor = instance['Monitoring']
            		instance_ids.append("[monitoring state] " + instance_monitor['State'])
	print("")
	print("")
	print("=================================")
	for i in instance_ids:
		print(i)
		if number % 5 == 0:
			print("=================================")
		number += 1
### 메인 함수###
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
		
		if number == 1:
			list_instance()

		elif number == 3:
			start_instance()
		elif number == 7:
			reboot_instance()
		
