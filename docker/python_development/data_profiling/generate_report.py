import json
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

# import sys
# print(sys.version)

df = pd.DataFrame(np.random.rand(1000, 5), columns=["a", "b", "c", "d", "e"])
# print(df)
#df.to_csv("data.csv")

missing_diagrams={
        "heatmap": False,
        "dendrogram": False,
    }

#profile = ProfileReport(df, title="Pandas Profiling Report")
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
json_data = profile.to_json()
profile_json = json.loads(json_data)
print("profile : ",profile_json.keys())
# dict_keys(['analysis', 'table', 'variables', 'scatter', 'correlations', 'missing', 'alerts', 'package', 'sample', 'duplicates']

#print("profile_json : ", profile_json.get("analysis"))
#{'title': 'Pandas Profiling Report', 'date_start': '2022-01-21 06:48:54.793291', 'date_end': '2022-01-21 06:48:58.130982', 'duration': '0:00:03.337691'}
#print("profile_json : ", profile_json.get("table"))
#{'n': 1000, 'n_var': 5, 'memory_size': 40128, 'record_size': 40.128, 'n_cells_missing': 0, 'n_vars_with_missing': 0, 'n_vars_all_missing': 0, 'p_cells_missing': 0.0, 'types': {'Numeric': 5}, 'n_duplicates': 0, 'p_duplicates': 0.0}
print("profile_json : ", profile_json.get("variables")[1])

# profile.to_file("your_report.json")
# profile.to_file("your_report.html")
