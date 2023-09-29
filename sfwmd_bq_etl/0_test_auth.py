"""
This script tests the authentication to BigQuery, Google Cloud Storage, and Google Earth Engine.
Authentication is done using the default credentials on the local machine.

If running on your local machine, you should authenticate first by running in your terminal:

    gcloud auth application-default login

"""

import sys

import ee
import google.auth
import google.oauth2.credentials
from google.cloud import bigquery
from google.cloud import storage

# Test if running in Google Colab
try:
    import google.colab  # noqa: F401
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

if IN_COLAB:
    # If running in Google Colab, set your project ID below!
    from google.colab import auth  # noqa: F401
    auth.authenticate_user(project_id="YOUR_PROJECT_ID")


def get_credentials():
    # Get the default credentials
    # We need to set the scopes to the ones we need for BigQuery, Google Cloud Storage, and Google Earth Engine
    # If we don't set the scopes, we will get an error when we try to authenticate to Google Earth Engine

    scopes = [
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/accounts.reauth",
        "https://www.googleapis.com/auth/earthengine",
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/devstorage.read_write",
    ]

    # Get the default credentials
    credentials, project_id = google.auth.default(scopes=scopes)

    # Google Earth Engine requires the quota project to be set to None (this is undocumented)
    credentials = credentials.with_quota_project(None)

    return credentials, project_id


def bigquery_auth(credentials, project_id):
    # Test authentication to BigQuery
    print("Testing authentication to BigQuery...")
    client = bigquery.Client(credentials=credentials, project=project_id)
    datasets = list(client.list_datasets())
    if datasets:
        print("BigQuery authentication successful!")
    else:
        print("BigQuery authentication failed!")
        sys.exit(1)


def gcs_auth(credentials, project_id):
    # Test authentication to Google Cloud Storage
    print("Testing authentication to Google Cloud Storage...")
    client = storage.Client(credentials=credentials, project=project_id)
    buckets = list(client.list_buckets())
    if buckets:
        print("Google Cloud Storage authentication successful!")
    else:
        print("Google Cloud Storage authentication failed!")
        sys.exit(1)


def gee_auth(credentials, project_id):
    # Test authentication to Google Earth Engine
    print("Testing authentication to Google Earth Engine...")
    try:
        # We have already authenticated to Google Earth Engine using the default credentials above,
        # so we don't need to run ee.Authenticate() here.
        # IGNORE THE GEE DOCS - ee.Authenticate() is not needed!
        # ee.Authenticate()  # This is not needed!

        ee.Initialize(credentials=credentials, project=project_id)

        # Test authentication by running a simple query
        image = ee.Image("srtm90_v4").getInfo()

        print("Google Earth Engine authentication successful!")
    except Exception as e:
        print("Google Earth Engine authentication failed!")
        print(e)
        raise e


def main():
    # Get the default credentials
    credentials, project_id = get_credentials()

    # Test authentication to BigQuery
    bigquery_auth(credentials, project_id)

    # Test authentication to Google Cloud Storage
    gcs_auth(credentials, project_id)

    # Test authentication to Google Earth Engine
    gee_auth(credentials, project_id)


if __name__ == "__main__":
    main()
