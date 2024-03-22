import pandas as pd
myDF = pd.read_csv('/anvil/projects/tdm/data/whin/weather.csv')
pd.set_option('display.max_columns', None)
myDF.head()
myDF.shape
myDF.describe()

myDF.value_counts('station_id')
myDF.groupby('station_id').size()

myDF.isnull().sum()
myDF.isnull().sum().sum()
myDF_cleaned = myDF.dropna()
myDF_cleaned.shape

myDFcleaned = myDF.dropna(subset=['temperature']).copy()
myDFcleaned.shape
myDFcleaned['location'] = myDFcleaned['latitude'].astype(str) + '_' + myDFcleaned['longitude'].astype(str)
myDFcleaned.groupby('location')['temperature'].mean()

def get_location_avgTemperature (df):
    dfclean = df.dropna(subset=['temperature']).copy()
    dfclean['location'] = dfclean['latitude'].astype(str) + '_' + dfclean['longitude'].astype(str)
    dfclean.groupby('location')['temperature'].mean()

myDFclean = myDF.dropna(subset=['wind_gust_speed_mph']).copy()
myDFclean['location'] = myDFclean['latitude'].astype(str) + '_' + myDFclean['longitude'].astype(str)
myDFclean.groupby('location')['wind_gust_speed_mph'].mean()

def get_location_avgWindGustSpeedMPH (df):
    dfclean = df.dropna(subset=['wind_gust_speed_mph']).copy()
    dfclean['location'] = dfclean['latitude'].astype(str) + '_' + dfclean['longitude'].astype(str)
    dfclean.groupby('location')['wind_gust_speed_mph'].mean()