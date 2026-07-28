import sounddevice as sd
import scipy.io.wavfile as wav


def record_audio(
        filename="input.wav",
        duration=5,
        samplerate=44100
):

    print("Listening...")


    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1
    )


    sd.wait()


    wav.write(
        filename,
        samplerate,
        recording
    )


    print("Recording saved")