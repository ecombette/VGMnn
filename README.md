# VGMnn

TensorFlow DNN (Deep Neural Network) classifier that classifies video games music (MIDI files) according to the game series they belong to. The results are however very poor and it is still under development, as DNN is not the appropriate model to classify such sequential data : it is being transformed into a RNN (Recurrent Neural Network), possibly with LSTM (Long Short Term Memory) cells.


The dataset we are using is for now made of video game music extracted from https://www.vgmusic.com. It is divided into three classes (Golden Sun, Mario and Zelda music), each of them containing about 50 MIDI files. From each file, we select the melody track for data preprocessing, the whole pipeline being processed using the [pretty_midi](https://github.com/craffel/pretty-midi) package.
