from fsspec.core import url_to_fs
import pandas as pd

class ReadWriter:

    def _init__(self):
        pass

    def get_filepaths(self, path):
        fs, urlpath = url_to_fs(path)
        return [f for f in fs.glob(urlpath) if not fs.isdir(f)]

    def read(self, file) -> pd.DataFrame:
        fs, urlpath = url_to_fs(path)
        try:
            fs.ls(file, detail=False)
        except FileNotFoundError:
            return pd.DataFrame()
        except NotADirectoryError:
            pass

        try:
            df = pq.read_table(
                file,
                filesystem=self.fs,
                use_legacy_dataset=True,
            ).to_pandas()
        except Exception as e:
            if self.data_spec.read_errors == Errors.ignore_errors:
                print(f"Failed to read {filepath}.\n{format_exc()}")
                df = pd.DataFrame()
            else:
                raise RuntimeError(
                    f"Error while reading {filepath}. If the file is invalid, "
                    f"remove it from the source before continuing."
                ) from e

        return df

    def read_csv(self, file) -> pd.DataFrame:
        return pd.read_csv(file)

# if __name__ == "__main__":
#     rw = ReadWriter()
# #    "s3://materion2noodle.blob.core.usgovcloudapi.net/incremental-data/sap/chemistry/2021/sap_chemistry_data_20210429120000.csv"
#     # for i in rw.get_filepaths("/Users/balakrishna.maduru/Documents/*"):
#     #     print(i)
#     filepaths = rw.get_filepaths("/Users/balakrishna.maduru/Documents/share_data/*")
#     for file in filepaths:
#         print(file)