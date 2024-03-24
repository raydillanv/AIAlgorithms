import time

import numpy as np
from matplotlib import pyplot as plt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# File paths
ins_file = 'unsplit_900x5_Shuf_4prior_0_diff_alignDCT_sent_ins.csv'
labs_file = 'unsplit_900x5_Shuf_4prior_0_diff_alignDCT_sent_labs.csv'

# Read inputs and labels
X = read_csv(ins_file, header=None)
y = read_csv(labs_file, header=None)

# Split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

def modelling(X_train, y_train, X_test, y_test):
    # Determine the number of input features
    n_features = X_train.shape[1]

    # Create model
    model = Sequential([
        Dense(128, activation='relu', input_shape=(n_features,)),
        Dense(64, activation='relu'),
        Dense(64, activation='relu'),
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

    # Return model at the end
    return model

def visualisation(X_test, y_test, model):
    # Evaluate
    mse = model.evaluate(X_test, y_test, verbose=0)
    print('MSE: %.3f, RMSE: %.3f' % (mse, np.sqrt(mse)))

    # A fairly simple visualisation, pick 6 at random and compare output to actual
    labelNo = [1500, 5789, 11370, 24, 501, 25999]

    fig = plt.figure()
    for i, label in enumerate(labelNo):
        # Extract data and convert to list
        row = X_test.iloc[label, :]
        row = row.values.reshape(1, -1)  # Reshape for model.predict

        # Predict output
        yhat = model.predict(row)

        # Get labels from test set
        lab = y_test.iloc[label, :]

        # Add a subplot
        ax = fig.add_subplot(3, 2, i+1)
        plt.plot(lab.values.flatten(), label='Actual')
        plt.plot(yhat.flatten(), label='Predicted', linestyle='--')
        plt.legend()

    plt.tight_layout()
    plt.show()

def extras_view_input_data(X_test, labelNo):
    # Extras, create a figure to look at the input data
    row = X_test.iloc[labelNo, :]
    row = row.values
    row = row.tolist()

    fig_inps = plt.figure()
    ax = fig_inps.add_subplot(111)
    ax.plot(row)
    plt.show()

def extras_view_label(y_test, labelNo):
    lab = y_test.iloc[labelNo,:]
    fig_inps = plt.figure()
    ax = fig_inps.add_subplot(111)
    ax.plot(lab)
    plt.show()

if __name__ == "__main__":
    start_time = time.time()
    model = modelling(X_train, y_train, X_test, y_test)
    visualisation(X_test, y_test, model)
    # Example usage of extras
    extras_view_input_data(X_test, 1500)
    extras_view_label(y_test, 1500)
    print("--- %s seconds ---" % (time.time() - start_time))
