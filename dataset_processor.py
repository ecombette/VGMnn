import os
import random
import pretty_midi
import numpy as np

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

def process_dataset(dataset_dir):
	dataset = []
	
	# Browse the MIDI files for each class
	for game in GAME_SERIES:
		trackfile = dataset_dir + '/' + game + '_tracks.txt'
		with open(trackfile) as fp:
			line = fp.readline()
			while line:
				file_info = line.split()
				print(file_info) # LOG
				# Retrieve the melody track from the MIDI file
				sequence = pretty_midi.PrettyMIDI(dataset_dir + '/' + game + '/' + file_info[0] + '.mid')
				track_matrix = np.zeros((100,4))
				track = sequence.instruments[int(file_info[1])]
				
				# Fill the notes in the matrix (no more than 100)
				track_size = len(track.notes) if len(track.notes) <=100 else 100
				for i in range(track_size):
					track_matrix[i] = track[i]
				
				# Add entry to dataset container
				dataset.append([track_matrix, game])
				line = fp.readline()
	
	# Randomize the dataset
	random.shuffle(dataset)
	
	# TO DO :
	# Fill the training set with the first 25 samples
	# Fill the evaluation set with the next 20 samples
	# Keep track of unused MIDI files for predictions?
	
	return [train_x, train_y], [eval_x, eval_y]

