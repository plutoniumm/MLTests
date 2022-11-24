import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# Scaling from 0-1
def Scale(data):
    scaler = MinMaxScaler()

    d_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    d_scaled = d_scaled[:1000]  # Temporary only 1000
    # Convert to float32 from 64 to increase speed
    d_scaled = d_scaled.astype('float32')
    return d_scaled


def processData(url):
    data = pd.read_csv(url)
    print(data.columns, "\n\n", data.shape)

    d_scaled = Scale(data)
    return d_scaled
