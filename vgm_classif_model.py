import tensorflow as tf
import dataset_processor

def main():
	print('TO DO main')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.register("type", "bool", lambda v: v.lower() == "true")
	parser.add_argument(
		"--dataset_dir",
		type=str,
		default="",
		help="Path to training data")
	FLAGS, _ = parser.parse_known_args()
	main()