import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Scaling from 0-1
def Scale(data):
    # scaler = MinMaxScaler()
    scaler = StandardScaler()

    d_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    # d_scaled = d_scaled[:1000]  # Temporary only 1000
    # Convert to float32 from 64 to increase speed
    d_scaled = d_scaled.astype('float32')
    return d_scaled


def xy_split(data, x_keys):
    x = data[x_keys]
    print("x: ", len(x_keys), " keys in ", len(x.columns), "cols")

    y_keys = list(set(data.columns) - set(x_keys))
    y = data[y_keys]
    print("y: ", len(y_keys), " keys in ", len(y.columns), "cols")
    return (x, y)

def xy_split_y(data, y_keys):
    x_keys = list(set(data.columns) - set(y_keys))

    x = data[x_keys]
    print("x: ", len(x_keys), " keys in ", len(x.columns), "cols")

    y = data[y_keys]
    print("y: ", len(y_keys), " keys in ", len(y.columns), "cols")
    return (x, y)


def processData(url):
    data = pd.read_csv(url)
    print(data.columns, "\n\n", data.shape)

    d_scaled = Scale(data)
    return d_scaled
