# VGMnn

TensorFlow DNN (Deep Neural Network) classifier that classifies video games music (MIDI files) according to the game series they belong to. It is however still under development, as a DNN is not the appropriate model to classify such sequential data : it is being transformed into a RNN (Recurrent Neural Network), possibly with LSTM (Long Short Term Memory) cells.


The dataset we are using is for now made of video game music extracted from https://www.vgmusic.com. It is divided into three classes (Golden Sun, Mario and Zelda music), each of them containing about 50 MIDI files with selection of the melody track for data preprocessing.
