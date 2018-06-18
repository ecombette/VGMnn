import argparse
import tensorflow as tf
import dataset_processor

def main():
	# Retrieve training and evaluation data
	[train_x, train_y], [eval_x, eval_y] = dataset_processor.process_data(FLAGS.dataset_dir)
	
	# Feature columns describe how to use the input.
    matrix_feature_column = tf.feature_column.numeric_column(key="Notes", shape=[100,4])

	# Build a DNN with 2 hidden layers and 10 nodes in each hidden layer.
    classifier = tf.estimator.DNNClassifier(
    feature_columns=matrix_feature_column,
    # Two hidden layers of 10 nodes each.
    hidden_units=[10, 10],
    # The model must choose between 3 classes (Zelda, Mario, Golden_Sun).
    n_classes=3)
	
	# Train the Model.
    classifier.train(
        input_fn=lambda:train_input_fn(train_x, train_y, FLAGS.batch_size),
        steps=FLAGS.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:eval_input_fn(test_x, test_y, FLAGS.batch_size))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
	print("TO DO : Generate predictions from the model")
	
    

def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    return dataset.shuffle(1000).repeat().batch(batch_size)

def eval_input_fn(features, labels, batch_size):
	"""An input function for evaluation or prediction"""
    features = dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)
	
	# Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.register("type", "bool", lambda v: v.lower() == "true")
	parser.add_argument(
		"--dataset_dir",
		type=str,
		default="",
		help="Path to training data")
	parser.add_argument(
		"--batch_size",
		default=50,
		type=int,
		help="Batch size")
	parser.add_argument(
		"--train_steps",
		default=1000,
		type=int,
		help="Number of training steps")
	FLAGS, _ = parser.parse_known_args()
	main()

