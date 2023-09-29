# SFWMD BigQuery to Earth Engine ETL
Example scripts for moving geographic data from BigQuery to Google Earth Engine

## Authentication
The scripts here assume that Application Default Credentials are set up on the machine running the scripts.
See [here](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more information.

To set up Application Default Credentials, run the following command in your terminal:
```
gcloud auth application-default login
```

### Google Colab
If you are running these scripts in Google Colab, you will not have access to a terminal and 
need to set up Application Default Credentials in a different way.
In the first cell of your Colab notebook, run the following:

```python
from google.colab import auth
auth.authenticate_user(project_id="YOUR_PROJECT_ID")
```

### Testing Credentials

To test that the credentials are set up correctly, you can run `0_test_auth.py`:
```shell
python sfwmd_bq_etl/0_test_auth.py
```