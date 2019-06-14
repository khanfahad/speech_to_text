from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("iqbal.mp3")
sound.export("transcript.wav", format="wav")
