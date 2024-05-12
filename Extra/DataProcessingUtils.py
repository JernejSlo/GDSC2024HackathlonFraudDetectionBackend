from datetime import datetime

import numpy as np
import pandas as pd

from Tests.Database import supabase


class DataProcessingUtils():
    def __init__(self, transaction_data_path, sort_by, user_data_path):
        data = pd.read_csv(transaction_data_path)
        # Group the data by the 'split_by' column
        self.grouped = data.groupby(sort_by)
        users = pd.read_csv(user_data_path)
        self.userDict = users.to_dict(orient='records')

    def get_user_age(self,user_id, data_dict):
        # Iterate over the list of dictionaries to find the user with the given ID
        for user in data_dict:
            if user['user_id'] == user_id:
                # Return the age of the user
                return user['age']

        # If the user ID is not found, return None
        return None

    def extract_and_update_user_model(self,transaction):
        UserInfo = self.fetch_row_by_id("UserInfo",transaction[1])

        # Flatten the group data into an array
        arr = transaction

        UserInfo['Age'] = self.get_user_age(arr[1], self.userDict)
        UserInfo['id'] = arr[1]
        # Count the number of transactions in each category
        UserInfo[arr[8]] += 1
        # Count the number of transactions in web,credit,debit,other
        UserInfo[arr[9]] += 1
        # Count the number of transactions in phone,computer,physical
        UserInfo[arr[10]] += 1

        if 0 < arr[2] < 10:
            UserInfo['SmallPayment'] += 1
        elif 10 < arr[2] < 50:
            UserInfo['MediumPayment'] += 1
        else:
            UserInfo['LargePayment'] += 1

        UserInfo['TotalTransactions'] += 1

        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
        time = datetime.fromtimestamp(int(arr[4])).strftime('%H:%M')
        if '00:00' <= time < '06:00':
            UserInfo['FirstPeriod'] += 1
            # print(time,"FirstPeriod")
        elif '06:00' <= time < '12:00':
            UserInfo['SecondPeriod'] += 1
            # print(time,"SecondPeriod")
        elif '12:00' <= time < '14:00':
            UserInfo['ThirdPeriod'] += 1
            # print(time,"ThirdPeriod")
        elif '14:00' <= time < '16:00':
            UserInfo['FourthPeriod'] += 1
            # print(time,"FourthPeriod")
        elif '16:00' <= time < '18:00':
            UserInfo['FifthPeriod'] += 1
            # print(time,"FifthPeriod")
        else:
            UserInfo['SixthPeriod'] += 1



        # update database here
        data, count = supabase.table('UserInfo').update(UserInfo).eq('id', arr[1]).execute()

    def fetch_row_by_id(self,table_name, row_id):
        data = supabase.table(table_name).select("*").eq('id', row_id).execute()
        return data.data[0]

    def extract_and_set_data(self):
        for name, group in self.grouped:
            UserInfo = {
                'Age': 0, 'id': 0, 'Groceries': 0, 'Shopping': 0, 'Restaurants': 0,
                'Travel': 0, 'Transport': 0, 'Entertainment': 0, 'Health': 0, 'General': 0,
                'Web': 0, 'Credit': 0, 'Debit': 0, 'Other': 0, 'FirstPeriod': 0, 'SecondPeriod': 0,
                'ThirdPeriod': 0, 'FourthPeriod': 0, 'FifthPeriod': 0, 'SixthPeriod': 0, 'Computer': 0,
                'Phone': 0, 'Physical': 0, 'SmallPayment': 0, 'MediumPayment': 0, 'LargePayment': 0,
                'TotalTransactions': 0
            }

            # Flatten the group data into an array
            array = group.to_numpy()

            for arr in array:
                UserInfo['Age'] = self.get_user_age(arr[1], self.userDict)
                UserInfo['id'] = arr[1]
                # Count the number of transactions in each category
                UserInfo[arr[8]] += 1
                # Count the number of transactions in web,credit,debit,other
                UserInfo[arr[9]] += 1
                # Count the number of transactions in phone,computer,physical
                UserInfo[arr[10]] += 1

                if 0 < arr[2] < 10:
                    UserInfo['SmallPayment'] += 1
                elif 10 < arr[2] < 50:
                    UserInfo['MediumPayment'] += 1
                else:
                    UserInfo['LargePayment'] += 1

                UserInfo['TotalTransactions'] += 1

                # if you encounter a "year is out of range" error the timestamp
                # may be in milliseconds, try `ts /= 1000` in that case
                time = datetime.fromtimestamp(int(arr[4])).strftime('%H:%M')
                if '00:00' <= time < '06:00':
                    UserInfo['FirstPeriod'] += 1
                    # print(time,"FirstPeriod")
                elif '06:00' <= time < '12:00':
                    UserInfo['SecondPeriod'] += 1
                    # print(time,"SecondPeriod")
                elif '12:00' <= time < '14:00':
                    UserInfo['ThirdPeriod'] += 1
                    # print(time,"ThirdPeriod")
                elif '14:00' <= time < '16:00':
                    UserInfo['FourthPeriod'] += 1
                    # print(time,"FourthPeriod")
                elif '16:00' <= time < '18:00':
                    UserInfo['FifthPeriod'] += 1
                    # print(time,"FifthPeriod")
                else:
                    UserInfo['SixthPeriod'] += 1
            print(UserInfo)
            data, count = supabase.table('UserInfo').insert(UserInfo).execute()

"""processor = DataProcessingUtils("./Tests/transactions.csv","UserId","./Tests/users.csv")
#processor.extract_and_set_data()
processor.extract_and_update_user_model([725,8,18.26,237,1451861703,0,0.0,0,"Travel","Other","Physical"])"""