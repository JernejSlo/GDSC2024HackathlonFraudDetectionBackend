class LoadUtils():
    def get_dataset_size(self,dataset):
        count = 0
        for _ in dataset:
            count += 1
        return count

    def define_test_and_train(self, dataset, percent_train):
        dataset_size = self.get_dataset_size(dataset)
        train_size = int(percent_train * dataset_size)

        train_dataset = dataset.take(train_size)
        test_dataset = dataset.skip(train_size)

        return train_dataset, test_dataset