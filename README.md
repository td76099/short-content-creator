# short-content-creator

Use a TTS program to generate the .wav file
Use lowerquality/gentle image with original input and .wav file to create the .srt
    - docker run -it --rm -v $(pwd):/tmp --entrypoint python lowerquality/gentle /gentle/align.py /tmp/output.mp3 /tmp/output.txt
FFMPEG it all together

python /gentle/align.py /tmp/output.mp3 /tmp/output.txt -o output.srt