import click
import boto3
import pandas as pd
import os
import io


def get_compressed_buffer(df):
	# print(df)
	csv_buffer = io.StringIO()
	df.to_csv(csv_buffer, index = False)
	return csv_buffer


def upload_file_to_s3(bucket_name, key, file_path):
	print(file_path)
	df = pd.read_csv(file_path)
	compressed_buff = get_compressed_buffer(df)
	s3 = boto3.client('s3')
	print(compressed_buff.getvalue())
	s3.put_object(Body = compressed_buff.getvalue(), Bucket = bucket_name, Key = key)
	return



@click.command()
@click.option('--file_path', default=None, help='File path of pnl file')
@click.option('--report_date', default=None, help='Latest complete UTC date in the format YYYY/MM/DD')
def main(file_path, report_date):
	file_name = os.path.split(file_path)[-1]

	bucket_name = os.environ['scife_client_bucket']
	s3_key = f"{os.environ['scife_client_folder']}/{report_date}/{file_name}"
	upload_file_to_s3(bucket_name, s3_key, file_path)
	return


if __name__ == '__main__':
	main()
