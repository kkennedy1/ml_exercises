import pandas as pd
import datetime

iowa_file_path = './home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

#print('hello there')
#print(home_data)
#home_data.describe()
#home_data.head()

val = int(round(home_data.LotArea.mean()))
print('val: %s' % val)

max_year = home_data.YearBuilt.max()
#print(datetime)
max_year_age = datetime.datetime.now().year - max_year
print('max: %s ' % max_year_age)