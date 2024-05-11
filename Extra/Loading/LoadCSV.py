import numpy as np
import pandas as pd
import tensorflow as tf
class LoadCSV:
    def parseCSV(self, data_path):
        df = pd.read_csv(data_path)
        df.to_numpy()
        numpy_array = df.to_numpy()

        array_of_arrays = np.array([np.array(row) for row in numpy_array])
        return array_of_arrays


    def parse_data_series_csv(self, data_path, split_by, n, target_column,num_classes):
        # Load the CSV using Pandas
        data = pd.read_csv(data_path)
        column_index = data.columns.get_loc(target_column)
        group_by_column = data.columns.get_loc(split_by)
        # Group the data by the 'split_by' column
        grouped = data.groupby(split_by)

        y = []


        # Dictionary to store the processed batches
        series_array = []
        # Process each group
        for name, group in grouped:
            # Flatten the group data into an array
            array = group.to_numpy()


            # Calculate how many full series of length 'n' can be created
            full_series_count = len(array) // n

            # Reshape the data to have 'full_series_count' of series, each of length 'n'
            if full_series_count > 0:
                series = array[:full_series_count * n].reshape(-1, n, array.shape[1])
                for series_ in series:
                    y.append([])
                    y[-1] = np.zeros(num_classes)
                    y[-1][int(series_[0][column_index])] = 1
                    y[-1] = np.asarray(y[-1])
                    series_array.append(np.delete(series_,column_index,1))
        series_array = np.asarray(series_array)
        y = np.asarray(y)
        print(series_array.shape)
        # Optionally convert series_dict to a more suitable format (e.g., tf.data.Dataset)
        # For now, we return the dictionary directly
        return series_array, y, group_by_column

"""# Example usage
data_path = '../../ML/Data/test_data.csv'
split_by = 'user_id'  # Column name to split by
sequence_length = 25  # Number of entries per time series sequence
X, y = LoadCSV().parse_data_series_csv(data_path, split_by, sequence_length,"time_since_last_here")

# To verify and inspect the processed data
for i in range(len(X)):
    #print("This is x: ",X[i],"This is y",y[i])
    continue"""


