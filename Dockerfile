#docker build --rm -t sound .
#docker run -it --privileged --device /dev/snd:/dev/snd sound
from python:3
run apt-get update
run apt-get install -y \
libasound-dev \
portaudio19-dev \
libportaudio2 \
libportaudiocpp0 \
ffmpeg \
alsa-utils
run git clone -b alsapatch https://github.com/gglockner/portaudio
run apt-get remove -y libportaudio2
run apt-get install -y libasound2-dev
run cd portaudio && ./configure && make && make install && ldconfig
run python -m pip install pyaudio
run python -m pip install SpeechRecognition
run mkdir -p /sound
copy read.py /sound/