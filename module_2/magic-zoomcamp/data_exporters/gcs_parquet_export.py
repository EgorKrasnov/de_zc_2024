# from mage_ai.settings.repo import get_repo_path
# from mage_ai.io.config import ConfigFileLoader
# from mage_ai.io.google_cloud_storage import GoogleCloudStorage
# from os import path
import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/src/key.json'
@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    # config_path = path.join(get_repo_path(), 'io_config.yaml')
    # config_profile = 'default'

    bucket_name = 'de_zc_week_2'
    object_key = 'green_taxi.parquet'
    table_name = 'ny_taxi'
    root_path = f'{bucket_name}/{table_name}'
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date

    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
            table,
            root_path=root_path,
            partition_cols=['lpep_pickup_date'],
            filesystem=gcs
    )
    return(0)
    # GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
    #     df,
    #     bucket_name,
    #     object_key,
    # )
