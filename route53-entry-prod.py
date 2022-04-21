import boto3
import csv


client = boto3.client('route53')

def add_cname_record(source, target):
	try:
		response = client.change_resource_record_sets(
		#add the hostzone ID 
		HostedZoneId='Z2JWGF3VP6Y9GB',
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (source, target),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': source,
								 'Type': 'CNAME',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': target}]
							}
						}]
		})
	except Exception as e:
		print (e)

if __name__ == "__main__":
	with open('domains.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			add_cname_record(row[0], row[1])