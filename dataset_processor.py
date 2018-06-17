import os
import argparse
import pretty_midi

def analyse_dataset(dataset_dir, classes):
	min = 1000
	max = 0
	smallsequences = []
	mean_size = 0
	num_sequences = 0
	
	for game in classes:
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
				if(sequence_size < 150): smallsequences.append([file_info[0], sequence_size])
				if(sequence_size < min): min = sequence_size
				if(sequence_size > max): max = sequence_size
				line = fp.readline()
	
	print('Min : ' + str(min))
	print('Max : ' + str(max))
	print('Nb of sequences : ' + str(num_sequences))
	print('Small sequences : ' + str(len(smallsequences)))
	print(smallsequences)
	print('Average sequence size : ' + str(mean_size / num_sequences))

def process_dataset(dataset_dir, classes):
	print('TO DO: process dataset')