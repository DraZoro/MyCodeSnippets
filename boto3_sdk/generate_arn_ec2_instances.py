#!/user/bin/env python 
import boto3

ec2_client = boto3.client('ec2')
sts_client = boto3.client('sts')

# Retrive the caller account 
account = sts_client.get_caller_identity()['Account']

# Retrive all the available regions 
regions = [region['RegionName']
          for region in ec2_client.describe_regions()['Regions']]

# Empty list to hold ARN 
ARN = []

# Iterate for per region 
for region in regions: 

    ec2 = boto3.resource('ec2', region_name=region)

    print("Active region:  {0}".format(region))

    # Pull all instances 
    instances = ec2.instances.filter()

    # print(instances)
    for instance in instances.all():

        # Only append if instance exist 
        if instance: 
           
           # ARN Format
           # arn:partition:service:region:account-id:resource-type/resource-id
           generate = "arn:aws:ec2:{0}:{1}:instance/{2}".format(region,account,instance.id)
           ARN.append(generate)

# Report the ARNs
for ins in ARN:
  
    print (ins)
