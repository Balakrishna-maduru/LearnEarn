import numpy as np
import pandas as pd
import pandas_profiling
def load_data():
    df = pd.DataFrame({'num_legs': [2, 4, 8, 0],'num_wings': [2, 0, 0, 0],'num_specimen_seen': [10, 2, 1, 8]},index=['falcon', 'dog', 'spider', 'fish'])
    print(df)
    profiler = df.profile_report(title='Test report', explorative=True,)
    profiler.to_file(output_file="output/gpl_profiler_output.html")
if __name__ == '__main__':
    load_data()
