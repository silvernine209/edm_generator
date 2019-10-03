# EDM Generator Using LSTM
In this project, I trained **LSTM models** to generate melody and percussion, which are then combined to generate **EDM music** with sprinkles of **Classical music**. Then, **nueral network classifier** was built to gauge output from LSTM models. Finally, **interactive Flask app** was built to utilize pretrained models to easily generate and play songs.

## Project Intro/Objective
I went to EDM concert for the first time in August 2019. Then, I wanted to generate my own **endless** EDM music, and this was done by infusing Classical music into it. Besides being unique, adding Classical music was very advantageous to overall flow and this will be discussed in "Feature Engineering" section. Also, **MIDI file format** was used for dataset, which means that instruments for generated melody and percussions can be altered very easily.

[Presentation Link - Google Slides](https://docs.google.com/presentation/d/1zXZ93rWshsaOpxh_lYr6b3dzsdWjL1Ek0-7hRlvWi_o/edit)  
[Presentation Link - Live](https://youtu.be/gTKVusBObZc)  
[Flask Demo](https://www.youtube.com/watch?v=-h8f86n0Ho0)

## Dataset Used
MIDI (Musical Instrument Digital Interface) file format was utilized in this project for data type of training set. First of many big advantages of MIDI format is that it is very **lightweight**, therefore very **scalable**. MIDI format is 0.05% in size compared to .wave format to represent similar length of sound. Also, because it is very lightweight, it is the perfect data type for Flask app in which EDM music is very quickly generated and played. Secondly, user can play generated melody and percussion with **ANY** type of instrument using MIDI player. Lastly and most importantly, notes are represented as 128 vectors in MIDI file format. This allowed very efficient and effective feature engineering process. Also, vector representaion of notes were key component of allowing LSTM models to generate very fluidic and pleasant melodies and percussions. Below are two sources from which MIDI files were obtained for EDM and Classical music. 

EDM - [Link](https://www.classicalarchives.com/midi.html)  
Classical - [Link](https://www.classicalarchives.com/midi.html)

## Methods Used
* AWS **(GPU-enabled cloud trainig)**
* Data Preprocessing
* Feature Engineering
* etc.

## Notable Technologies Used
* Python 3, Jupyter Notebook
* Pypianoroll, Music21 **(MIDI file format encoder/decoder/player)**
* Pandas, Numpy, Matplotlib, Seaborn **(Data Processing/Visualization tools)**
* TensorFlow, Keras, Scikit-learn **(LSTM and Neural Network Models)**
* Flask **(Demo generation)**
* etc. 

## Feature Engineering

## Model 
![models](img/models.jpg)

## Result 
![results](img/result.JPG)

## Conclusion

