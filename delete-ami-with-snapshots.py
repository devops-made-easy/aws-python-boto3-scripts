import boto3
client = boto3.client('ec2')

image_id = 'ami-xxxxx'


images_list = client.describe_images(
    ImageIds=[
        image_id,
    ]
)['Images'][0]

delete_image = client.deregister_image(
    ImageId=image_id,
)
print("===> Deleted image with id " + image_id)
print(delete_image)

for snapshot in images_list['BlockDeviceMappings']:
    print("===> Deleting Snapshot: " + snapshot['Ebs']['SnapshotId'])
    delete_snapshot = client.delete_snapshot(
        SnapshotId=snapshot['Ebs']['SnapshotId'],
    )
    print(delete_snapshot)
