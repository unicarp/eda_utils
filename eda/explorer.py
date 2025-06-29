import pandas as pd

class Explorer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self._validate_dataframe()

    def _validate_dataframe(self):
        """Validates that the input is a pandas DataFrame and is not empty."""
        if not isinstance(self.df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        if self.df.empty:
            raise ValueError("DataFrame is empty.")

    def first_summary(self, as_dict=False, print_all=False):
        """ Returns a summary of the DataFrame including shape, columns, dtypes and describe,
            all of them in a dictionary format. These are typically used as the first steps in EDA.
            Use `as_dict=False` to return pandas objects.
            If you want to return the summary as a dictionary —easy-to-use for JSONs or APIs—,
            set `as_dict=True`."""
        if as_dict:
            summary = {
                "shape": self.df.shape,
                "columns": self.df.columns.tolist(),
                "dtypes": self.df.dtypes.astype(str).to_dict(),
                "describe": self.df.describe(include="all").to_dict()
            }
        else:
            summary = {
                "shape": self.df.shape,
                "columns": self.df.columns,
                "dtypes": self.df.dtypes,
                "describe": self.df.describe(include="all")
            }

        if print_all:
            print("\u001b[32mDataFrame initial Summary:\u001b[0m\n")
            for key in summary:
                print(f"\u001b[34m>> {key.upper()}:\u001b[0m\n")
                print(summary[key], "\n")

        return summary