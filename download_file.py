import click
import boto3
import os
import json




@click.command()
@click.option('--report_date', default=None, help='Latest complete UTC date in the format YYYY/MM/DD')
def main(report_date):


	bucket_name = os.environ['scife_read_bucket']
	s3_prefix = f"{os.environ['scife_read_folder']}/{report_date}"


	client = boto3.client('s3')
	response = client.list_objects(
	    Bucket=bucket_name,
	    Prefix=s3_prefix
	)

	file_list = response['Contents']

	print("Files to download ----")
	for file in file_list:
		print(file['Key'])
		client.download_file(bucket_name, file['Key'], os.path.split(file['Key'])[-1])

	return


if __name__ == '__main__':
	main()

