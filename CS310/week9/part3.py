import time

import numpy as np
from matplotlib import pyplot as plt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# File paths
ins_file = 'unsplit_900x5_Shuf_4prior_0_diff_alignDCT_sent_ins.csv'
labs_file = 'unsplit_900x5_Shuf_4prior_0_diff_alignDCT_sent_labs.csv'

# Read inputs and labels
X = read_csv(ins_file, header=None)
y = read_csv(labs_file, header=None)

# Split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Reshape data to [samples, time_steps, features_per_frame]
n_frames = 4
n_features_per_frame = X_train.shape[1] // n_frames
X_train_reshaped = X_train.values.reshape(-1, n_frames, n_features_per_frame)
X_test_reshaped = X_test.values.reshape(-1, n_frames, n_features_per_frame)

def modelling(X_train, y_train, X_test, y_test):
    # Determine the number of features per frame and the number of frames
    n_features_per_frame = X_train.shape[2]
    n_frames = X_train.shape[1]

    # Create model
    model = Sequential([
        SimpleRNN(128, activation='tanh', input_shape=(n_frames, n_features_per_frame)),
        Dense(64, activation='relu'),
        Dense(23)  # Output layer with 23 neurons for the 23 components
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

    # Evaluate the model
    mse = model.evaluate(X_test, y_test, verbose=0)
    print('MSE: %.3f' % mse)

    return model

def visualisation(X_test, y_test, model):
    # Evaluate
    mse = model.evaluate(X_test, y_test, verbose=0)
    print('MSE: %.3f, RMSE: %.3f' % (mse, np.sqrt(mse)))

    # A fairly simple visualisation, pick 6 at random and compare output to actual
    labelNo = [1500, 5789, 11370, 24, 501, 25999]

    fig = plt.figure()
    for i, label in enumerate(labelNo):
        # shape row correctly matching the input shape expected by model
        row = X_test[label, :, :].reshape(1, 4, 24)

        # Predict output
        yhat = model.predict(row)

        # Handling y_test based on whether it's a DataFrame or a NumPy array
        if hasattr(y_test, 'iloc'):
            lab = y_test.iloc[label, :].values  # Convert to NumPy array if y_test is DataFrame
        else:
            lab = y_test[label, :]

        # Add a subplot
        ax = fig.add_subplot(3, 2, i+1)
        plt.plot(lab.flatten(), label='Actual')  # guarantor to be a NumPy array
        plt.plot(yhat.flatten(), label='Predicted', linestyle='--')
        plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    start_time = time.time()
    model = modelling(X_train_reshaped, y_train, X_test_reshaped, y_test)
    visualisation(X_test_reshaped, y_test, model)
    print("--- %s seconds ---" % (time.time() - start_time))
