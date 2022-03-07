from enum import Enum

class ReportGeneratorConstant(Enum):
    # Common constants
    PROCSSES_ID = "procsses_id"
    START_TIME = "start_time"
    END_TIME = "end_time"
    FILE_NAME = "file_name"
    PROCESSED_TIME = "processed_time"
    # Dataset metadata
    TYPE_OF_DATA = "type_of_data"
    NUMBER_OF_ATTRIBUTES = "number_of_attributes"
    NUMBER_OF_OBSERVATIONS = "number_of_observations"
    MISSING_CELLS_PERCENTAGE = "missing_cells_percentage"
    DUPLICATE_ROWS_PERCENTAGE = "duplicate_rows_percentage"
    TOTAL_SIZE_IN_MEMORY = "total_size_in_memory"
    # Attribute metadata
    ATTRIBUTE_NAME = "attribute_name"
    TYPE_OF_ATTRIBUTE = "type_of_attribute"
    ATTRIBUTE_DETAILS = "attribute_details"
    DISTINCT_PERCENTAGE = "distinct_percentage"
    MISSING_PERCENTAGE = "missing_percentage"
    UNIQUE_PERCENTAGE = "unique_percentage"
    NEGATIVE_PERCENTAGE = "negative_percentage"
    ZEROS_PERCENTAGE = "zeros_percentage"
    MEAN = "mean"
    MIN = "min"
    MAX = "max"

    # json variables
    NUMBER_OF_ROWS = "n"
    N_VAR = "n_var"
    P_CELLS_MISSING = "p_cells_missing"
    P_DUPLICATES = "p_duplicates"
    MEMORY_SIZE = "memory_size"
    P_DISTINCT = "p_distinct"
    P_MISSING = "p_missing"
    P_UNIQUE = "p_unique"
    P_NEGATIVE = "p_negative"
    P_ZEROS = "p_zeros"
    TYPE = "type"
    IS_UNIQUE = "is_unique"

class DataProfileDefault(Enum):
    TABLE = "table"
    VARIABLES = "variables"
    DATASET_METADATA = "dataset_metadata"
    ATTRIBUTE_METADATA = "attribute_metadata"
    NUMERIC = "numeric"
    CATEGORICAL = "categorical"
