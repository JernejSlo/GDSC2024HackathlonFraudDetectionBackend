import tensorflow as tf


class LoadCSV:
    def parseCSV(self, data_path):
        # Create a TensorFlow dataset from the CSV file
        dataset = tf.data.experimental.make_csv_dataset(
            file_pattern=data_path,
            batch_size=1,  # Adjust the batch size according to your needs
            num_epochs=1,  # Number of times to read the input data
            ignore_errors=True  # Continue with remaining data if there are errors
        )

        return dataset

loader = LoadCSV()
data_path = '../../ML/Data/Match.csv'
dataset = loader.parseCSV(data_path)
print(dataset)