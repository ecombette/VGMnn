import os
import random
import pretty_midi

GAME_SERIES = ['Golden_Sun', 'Mario', 'Zelda']

def analyse_dataset(dataset_dir):
# Utility function for analyzing our dataset
	min = 1000
	max = 0
	smallsequences = []
	mean_size = 0
	num_sequences = 0
	
	for game in GAME_SERIES:
		trackfile = dataset_dir + '/' + game + '_tracks.txt'
		with open(trackfile) as fp:
			line = fp.readline()
			while line:
				num_sequences += 1
				file_info = line.split()
				print(file_info)
				sequence = pretty_midi.PrettyMIDI(dataset_dir + '/' + game + '/' + file_info[0] + '.mid')
				track = sequence.instruments[int(file_info[1])]
				sequence_size = len(track.notes)
				mean_size += sequence_size
				if(sequence_size < 100): smallsequences.append([file_info[0], sequence_size])
				if(sequence_size < min): min = sequence_size
				if(sequence_size > max): max = sequence_size
				line = fp.readline()
	
	print('Min : ' + str(min))
	print('Max : ' + str(max))
	print('Nb of sequences : ' + str(num_sequences))
	print('Small sequences : ' + str(len(smallsequences)))
	print(smallsequences)
	print('Average sequence size : ' + str(mean_size / num_sequences))

def process_data(dataset_dir):
	dataset = []
	min_pitch = 1000
	min_duration = 1000
	min_velocity = 1000
	max_pitch = 0
	max_duration = 0
	max_velocity = 0
	# Browse the MIDI files for each class
	for game in GAME_SERIES:
		trackfile = dataset_dir + '/' + game + '_tracks.txt'
		with open(trackfile) as fp:
			line = fp.readline()
			while line:
				file_info = line.split()
				#print(file_info)
				
				# Retrieve the melody track from the MIDI file
				sequence = pretty_midi.PrettyMIDI(dataset_dir + '/' + game + '/' + file_info[0] + '.mid')
				track_matrix = []
				track = sequence.instruments[int(file_info[1])].notes
				
				# Fill the notes in the matrix (the first 100 notes at most)
				track_size = len(track) if len(track) <=100 else 100
				for i in range(track_size):
					if track[i].pitch < min_pitch: min_pitch = track[i].pitch
					if track[i].pitch > max_pitch: max_pitch = track[i].pitch
					if track[i].end - track[i].start < min_duration: min_duration = track[i].end - track[i].start
					if track[i].end - track[i].start > max_duration: max_duration = track[i].end - track[i].start
					if track[i].velocity < min_velocity: min_velocity = track[i].velocity
					if track[i].velocity > max_velocity: max_velocity = track[i].velocity
					track_matrix.append([track[i].pitch, track[i].end - track[i].start, track[i].velocity])
				if track_size < 100:
					for i in range(track_size, 100):
						track_matrix.append([0., 0., 0.])
				
				# Add entry to dataset container
				dataset.append([track_matrix, GAME_SERIES.index(game), file_info[0]])
				line = fp.readline()
	
	# Randomize the dataset
	random.shuffle(dataset)
	
	# Normalize dataset
	for entry in range(len(dataset)):
		for i in range(100):
			if dataset[entry][0][i][0] != 0:
				dataset[entry][0][i][0] = 1 + (dataset[entry][0][i][0] - min_pitch) / (max_pitch - min_pitch)
			if dataset[entry][0][i][1] != 0:
				dataset[entry][0][i][1] = 1 + (dataset[entry][0][i][1] - min_duration) / (max_duration - min_duration)
			if dataset[entry][0][i][2] != 0:
				dataset[entry][0][i][2] = 1 + (dataset[entry][0][i][2] - min_velocity) / (max_velocity - min_velocity)
	
	# Fill the training set with the first 105 samples
	train_x = {"Notes" : []}
	train_y = []
	for i in range(105):
		train_x["Notes"].append(dataset[i][0])
		train_y.append(dataset[i][1])
	
	# Fill the evaluation set with the next 30 samples
	eval_x = {"Notes" : []}
	eval_y = []
	for i in range(105,135):
		eval_x["Notes"].append(dataset[i][0])
		eval_y.append(dataset[i][1])
	
	# TO DO : Keep track of unused MIDI files for predictions
	test_x = {"Notes" : []}
	test_y = []
	print("Prediction files :")
	for i in range(135, len(dataset)):
		test_x["Notes"].append(dataset[i][0])
		test_y.append(dataset[i][1])
		print(dataset[i][2])
	
	return [train_x, train_y], [eval_x, eval_y], [test_x, test_y]

def normalize_dataset(dataset):

	return dataset

