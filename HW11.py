{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5d7f53c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "bb8b95cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('california_housing_test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "72f0766d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3402, 9)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9b9048c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0              int64\n",
       "longitude             float64\n",
       "latitude              float64\n",
       "housing_median_age      int64\n",
       "total_rooms             int64\n",
       "total_bedrooms          int64\n",
       "population              int64\n",
       "households              int64\n",
       "median_income         float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dcd727f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['longitude', 'latitude', 'housingMedianAge', 'totalRooms',\n",
       "       'totalBedrooms', 'population', 'households', 'medianIncome',\n",
       "       'medianHouseValue'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6d5dbf3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>longitude</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-117.66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-117.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-117.91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-117.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-119.58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3392</th>\n",
       "      <td>-122.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3393</th>\n",
       "      <td>-117.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3395</th>\n",
       "      <td>-117.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3398</th>\n",
       "      <td>-117.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3399</th>\n",
       "      <td>-118.32</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2216 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      longitude\n",
       "0       -117.66\n",
       "1       -117.07\n",
       "2       -117.91\n",
       "3       -117.19\n",
       "4       -119.58\n",
       "...         ...\n",
       "3392    -122.10\n",
       "3393    -117.52\n",
       "3395    -117.01\n",
       "3398    -117.88\n",
       "3399    -118.32\n",
       "\n",
       "[2216 rows x 1 columns]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['housing_median_age'] < 35, ['longitude']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0b120de8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>longitude</th>\n",
       "      <th>latitude</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-117.66</td>\n",
       "      <td>35.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-117.07</td>\n",
       "      <td>32.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-117.91</td>\n",
       "      <td>33.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-117.19</td>\n",
       "      <td>34.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-119.58</td>\n",
       "      <td>36.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3397</th>\n",
       "      <td>-118.33</td>\n",
       "      <td>34.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3398</th>\n",
       "      <td>-117.88</td>\n",
       "      <td>34.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3399</th>\n",
       "      <td>-118.32</td>\n",
       "      <td>34.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3400</th>\n",
       "      <td>-118.12</td>\n",
       "      <td>33.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3401</th>\n",
       "      <td>-118.19</td>\n",
       "      <td>33.78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3402 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      longitude  latitude\n",
       "0       -117.66     35.60\n",
       "1       -117.07     32.71\n",
       "2       -117.91     33.61\n",
       "3       -117.19     34.05\n",
       "4       -119.58     36.83\n",
       "...         ...       ...\n",
       "3397    -118.33     34.09\n",
       "3398    -117.88     34.09\n",
       "3399    -118.32     34.26\n",
       "3400    -118.12     33.80\n",
       "3401    -118.19     33.78\n",
       "\n",
       "[3402 rows x 2 columns]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['longitude', 'latitude']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "8d0cf96b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>longitude</th>\n",
       "      <th>latitude</th>\n",
       "      <th>housing_median_age</th>\n",
       "      <th>total_rooms</th>\n",
       "      <th>total_bedrooms</th>\n",
       "      <th>population</th>\n",
       "      <th>households</th>\n",
       "      <th>median_income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>-118.21</td>\n",
       "      <td>33.79</td>\n",
       "      <td>39</td>\n",
       "      <td>1598</td>\n",
       "      <td>458</td>\n",
       "      <td>1691</td>\n",
       "      <td>399</td>\n",
       "      <td>2.3605</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>19</td>\n",
       "      <td>-122.41</td>\n",
       "      <td>37.80</td>\n",
       "      <td>30</td>\n",
       "      <td>1821</td>\n",
       "      <td>738</td>\n",
       "      <td>1648</td>\n",
       "      <td>684</td>\n",
       "      <td>0.8836</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>70</td>\n",
       "      <td>-117.93</td>\n",
       "      <td>34.01</td>\n",
       "      <td>33</td>\n",
       "      <td>1733</td>\n",
       "      <td>361</td>\n",
       "      <td>1757</td>\n",
       "      <td>375</td>\n",
       "      <td>4.2266</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>101</td>\n",
       "      <td>-121.24</td>\n",
       "      <td>36.33</td>\n",
       "      <td>13</td>\n",
       "      <td>1642</td>\n",
       "      <td>418</td>\n",
       "      <td>1534</td>\n",
       "      <td>388</td>\n",
       "      <td>3.1222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>121</td>\n",
       "      <td>-118.22</td>\n",
       "      <td>33.90</td>\n",
       "      <td>35</td>\n",
       "      <td>1649</td>\n",
       "      <td>424</td>\n",
       "      <td>1786</td>\n",
       "      <td>388</td>\n",
       "      <td>1.4091</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3151</th>\n",
       "      <td>3152</td>\n",
       "      <td>-118.36</td>\n",
       "      <td>34.22</td>\n",
       "      <td>37</td>\n",
       "      <td>1512</td>\n",
       "      <td>348</td>\n",
       "      <td>1545</td>\n",
       "      <td>351</td>\n",
       "      <td>3.7663</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3172</th>\n",
       "      <td>3173</td>\n",
       "      <td>-117.89</td>\n",
       "      <td>33.74</td>\n",
       "      <td>32</td>\n",
       "      <td>1562</td>\n",
       "      <td>365</td>\n",
       "      <td>2145</td>\n",
       "      <td>347</td>\n",
       "      <td>2.9167</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3215</th>\n",
       "      <td>3216</td>\n",
       "      <td>-118.23</td>\n",
       "      <td>33.92</td>\n",
       "      <td>32</td>\n",
       "      <td>1735</td>\n",
       "      <td>430</td>\n",
       "      <td>1699</td>\n",
       "      <td>386</td>\n",
       "      <td>1.1793</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3332</th>\n",
       "      <td>3333</td>\n",
       "      <td>-119.76</td>\n",
       "      <td>36.71</td>\n",
       "      <td>29</td>\n",
       "      <td>1745</td>\n",
       "      <td>441</td>\n",
       "      <td>1530</td>\n",
       "      <td>391</td>\n",
       "      <td>1.5611</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3372</th>\n",
       "      <td>3373</td>\n",
       "      <td>-118.20</td>\n",
       "      <td>33.99</td>\n",
       "      <td>35</td>\n",
       "      <td>1705</td>\n",
       "      <td>523</td>\n",
       "      <td>2252</td>\n",
       "      <td>508</td>\n",
       "      <td>2.3421</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>106 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Unnamed: 0  longitude  latitude  housing_median_age  total_rooms  \\\n",
       "12            13    -118.21     33.79                  39         1598   \n",
       "18            19    -122.41     37.80                  30         1821   \n",
       "69            70    -117.93     34.01                  33         1733   \n",
       "100          101    -121.24     36.33                  13         1642   \n",
       "120          121    -118.22     33.90                  35         1649   \n",
       "...          ...        ...       ...                 ...          ...   \n",
       "3151        3152    -118.36     34.22                  37         1512   \n",
       "3172        3173    -117.89     33.74                  32         1562   \n",
       "3215        3216    -118.23     33.92                  32         1735   \n",
       "3332        3333    -119.76     36.71                  29         1745   \n",
       "3372        3373    -118.20     33.99                  35         1705   \n",
       "\n",
       "      total_bedrooms  population  households  median_income  \n",
       "12               458        1691         399         2.3605  \n",
       "18               738        1648         684         0.8836  \n",
       "69               361        1757         375         4.2266  \n",
       "100              418        1534         388         3.1222  \n",
       "120              424        1786         388         1.4091  \n",
       "...              ...         ...         ...            ...  \n",
       "3151             348        1545         351         3.7663  \n",
       "3172             365        2145         347         2.9167  \n",
       "3215             430        1699         386         1.1793  \n",
       "3332             441        1530         391         1.5611  \n",
       "3372             523        2252         508         2.3421  \n",
       "\n",
       "[106 rows x 9 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[(df['total_rooms'] < 2000) & (df['population'] > 1500)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "980393a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "35682\n"
     ]
    }
   ],
   "source": [
    "print(df['population'].min())\n",
    "print(df['population'].max())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "72613678",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-124.18"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['median_income'] > 3]['longitude'].min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "deba371c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['households'] == df['households'].min()]['total_bedrooms'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d0d7738",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
