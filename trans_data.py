import pandas as pd


hotel_data = pd.read_csv('hotel_data1.csv')
hotel_data['room_price'].str.split('£', expand=True)
print(hotel_data.head())