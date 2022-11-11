import pandas as pd


hotel_data = pd.read_csv('hotel_data1.csv')
hotel_data['price (£)'] = hotel_data['room_price'].str.replace('£', '')
#
hotel_data['price (£)'].str.replace(',', '', regex=True)
hotel_data['price (£)'].str.strip()
hotel_data['price (£)'] = hotel_data['price (£)'].apply(pd.to_numeric,errors='coerce')

hotel_data['total_reviews'] = hotel_data['total_reviews'].str.replace(' reviews', '', regex=True)
hotel_data['total_reviews'] = hotel_data['total_reviews'].str.replace(',', '', regex=True)
hotel_data['total_reviews'] = hotel_data['total_reviews'].apply(pd.to_numeric,errors='coerce')
print(hotel_data.head())

desc_groupby = hotel_data.groupby(['rating_desciption','price (£)'])['total_reviews'].aggregate(['mean', 'count'])


result = hotel_data.groupby(['rating_desciption','price (£)']).mean()
print(result)