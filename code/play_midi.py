import pygame

def play_music1(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print ("Music file %s loaded!" % music_file)
    except pygame.error:
        print ("File %s not found! (%s)" % (music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
        
def play_music(music_file):
    # Play Midi file
    try:
        play_music1(music_file)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit
        
def play_music_csv(music_csv):        
    # Parse the CSV output of the previous command back into a MIDI file
    midi_object = py_midicsv.csv_to_midi(music_csv)

    # Save the parsed MIDI file to disk
    with open("example_converted.mid", "wb") as output_file:
        midi_writer = py_midicsv.FileWriter(output_file)
        midi_writer.write(midi_object)
    play_music("example_converted.mid")