import tensorflow as tf

from Extra.Loading.LoadUtils import LoadUtils


class LoadCSV:
    def parseCSV(self, data_path):
        # Create a TensorFlow dataset from the CSV file
        dataset = tf.data.experimental.make_csv_dataset(
            file_pattern=data_path,
            batch_size=1,  # Adjust the batch size according to your needs
            num_epochs=1,  # Number of times to read the input data
        )

        return dataset

