# s3-scripts
Repo to upload / download scripts to S3


# To Install : 

```
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

# Set the environment variables :

We will share two envornment variables, `scife_bucket` and `scife_client_folder` please set them before executing the script.


# Sample run command to upload the file:

```
python upload_file.py --file_path=pnl_daily.csv --report_date=2019/01/02
```

Here `file_path` is the path to any CSV file. `report_date` is the day for till which the PNL is computed. Please note, if you execute the same command again, the old file will be overwritten.

Ideally you should generate your PNL file after UTC 12 Noon. Say right now UTC date is 2019-12-25 and time is 12:30 PM UTC. Then set report date as `2019/12/25` ie year, month and date.


# Sample run command to download the file:
