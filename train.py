def input_evaluation_set():
    features = {'Music':  np.array([2.8, 2.3]),
    labels = np.array(1)
    return features, labels


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    return dataset.shuffle(1000).repeat().batch(batch_size)

                
# Feature columns describe how to use the input.
    matrix_feature_column = tf.feature_column.numeric_column(key="Music",
                                                       shape=[4,1])

# Build a DNN with 2 hidden layers and 10 nodes in each hidden layer.
    classifier = tf.estimator.DNNClassifier(
    feature_columns=matrix_feature_column,
    # Two hidden layers of 10 nodes each.
    hidden_units=[10, 10],
    # The model must choose between 3 classes (Zelda, Mario, Golden_Sun).
    n_classes=3)
