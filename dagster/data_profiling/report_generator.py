import os
import json
import numpy as np
import pandas as pd
from datetime import datetime
from dagster import get_dagster_logger
from pandas_profiling import ProfileReport
from data_store.db_manager import DBConnection
from constant.constant import DataProfileDefault as dpc
from constant.constant import ReportGeneratorConstant as rgc


class ReportGenerator:
    def __init__(self, type_of_data="") -> None:
        self.__file_data = {}
        self.__type_of_data = type_of_data
        self.__db_connection = DBConnection.instance()
        self._processed_id = self.get_processed_id
        self._processed_time = datetime.now()

    @property
    def get_processed_id(self):
        id = self.__db_connection.select(
            f"select max({rgc.PROCSSES_ID.value}) from {dpc.DATASET_METADATA.value}").first()[0]
        if id:
            return id
        return 1

    def generate(self, df, html_output_dir, file):
        self.__file_name = file
        missing_diagrams = {
            "heatmap": False,
            "dendrogram": False,
        }
        correlations = {
            "pearson": {"calculate": False},
            "spearman": {"calculate": False},
            "kendall": {"calculate": False},
            "phi_k": {"calculate": False},
            "cramers": {"calculate": False},
        }
        profile = ProfileReport(df,
                                title=self.__file_name,
                                explorative=True,
                                # missing_diagrams = missing_diagrams,
                                # correlations = correlations
                                )
        self.__json_data = json.loads(profile.to_json())
        self._get_dataset_metadata()
        self._get_attibute_metadata()
        self._insert_data()
        self.write_html_file(profile, html_output_dir)

    def _get_dataset_metadata(self):
        get_dagster_logger().info(
            f"Dataset metadata : {self.__json_data[dpc.TABLE.value]}")
        table_attributes = self.__json_data[dpc.TABLE.value]

        self.__file_data[dpc.DATASET_METADATA.value] = {rgc.PROCSSES_ID.value: self._processed_id,
                                                        rgc.START_TIME.value: datetime.now(),
                                                        rgc.END_TIME.value: datetime.now(),
                                                        rgc.TYPE_OF_DATA.value: self.__type_of_data,
                                                        rgc.FILE_NAME.value: self.__file_name,
                                                        rgc.PROCESSED_TIME.value: self._processed_time,
                                                        rgc.NUMBER_OF_ATTRIBUTES.value: table_attributes[rgc.N_VAR.value],
                                                        rgc.NUMBER_OF_OBSERVATIONS.value: table_attributes[rgc.NUMBER_OF_ROWS.value],
                                                        rgc.MISSING_CELLS_PERCENTAGE.value: table_attributes[rgc.P_CELLS_MISSING.value],
                                                        rgc.DUPLICATE_ROWS_PERCENTAGE.value: table_attributes[rgc.P_DUPLICATES.value],
                                                        rgc.TOTAL_SIZE_IN_MEMORY.value: table_attributes[
                                                            rgc.MEMORY_SIZE.value]
                                                        }

    def _get_attibute_metadata(self):
        attribute_medata_data = []
        for column, values in self.__json_data[dpc.VARIABLES.value].items():
            # get_dagster_logger().info(f"{column} values : {values}")
            if values['type'].lower() == dpc.NUMERIC.value:
                self._numeric_type(column, values, attribute_medata_data)
            elif values['type'].lower() == dpc.CATEGORICAL.value:
                self._categorical_type(column, values, attribute_medata_data)
            else:
                get_dagster_logger().info(f"Specified category not handled..!")
        self.__file_data[dpc.ATTRIBUTE_METADATA.value] = attribute_medata_data

    def _numeric_type(self, column, values, attribute_medata_data):
        attribute_medata_data.append({rgc.PROCSSES_ID.value: self._processed_id,
                                      rgc.ATTRIBUTE_NAME.value: column,
                                      rgc.TYPE_OF_ATTRIBUTE.value: values[rgc.TYPE.value],
                                      rgc.PROCESSED_TIME.value: self._processed_time,
                                      rgc.ATTRIBUTE_DETAILS.value: {
                                          rgc.DISTINCT_PERCENTAGE.value: values[rgc.P_DISTINCT.value],
                                          rgc.MISSING_CELLS_PERCENTAGE.value: values[rgc.P_MISSING.value],
                                          rgc.UNIQUE_PERCENTAGE.value: values[rgc.P_UNIQUE.value],
                                          rgc.NEGATIVE_PERCENTAGE.value: values[rgc.P_NEGATIVE.value],
                                          rgc.ZEROS_PERCENTAGE.value: values[rgc.P_ZEROS.value],
                                          rgc.MEAN.value: values[rgc.MEAN.value],
                                          rgc.MIN.value: values[rgc.MIN.value],
                                          rgc.MAX.value: values[rgc.MAX.value]
                                      }  # need to look
                                      })

    def _categorical_type(self, column, values, attribute_medata_data):
        attribute_medata_data.append({rgc.PROCSSES_ID.value: self._processed_id,
                                      rgc.ATTRIBUTE_NAME.value: column,
                                      rgc.TYPE_OF_ATTRIBUTE.value: values[rgc.TYPE.value],
                                      rgc.PROCESSED_TIME.value: self._processed_time,
                                      rgc.ATTRIBUTE_DETAILS.value: {
                                          rgc.DISTINCT_PERCENTAGE.value: values[rgc.P_DISTINCT.value],
                                          rgc.MISSING_CELLS_PERCENTAGE.value: values[rgc.P_MISSING.value],
                                          rgc.UNIQUE_PERCENTAGE.value: values[rgc.P_UNIQUE.value],
                                          rgc.IS_UNIQUE.value: values[rgc.IS_UNIQUE.value]
                                      }
                                      })

    def _insert_data(self):
        self.__db_connection.insert(
            dpc.DATASET_METADATA.value, self.__file_data[dpc.DATASET_METADATA.value])
        self.__db_connection.insert(
            dpc.ATTRIBUTE_METADATA.value, self.__file_data[dpc.ATTRIBUTE_METADATA.value])

    def write_html_file(self, profile, path):
        file = os.path.splitext(os.path.basename(self.__file_name))[0]
        file = f"{path}/{file}.html"
        profile.to_file(file)
