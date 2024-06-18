# short-content-creator

Use a TTS program to generate the .wav file
Use lowerquality/gentle image with original input and .wav file to create the .srt
    - docker run -it --rm -v $(pwd):/tmp --entrypoint python lowerquality/gentle /gentle/align.py /tmp/output.mp3 /tmp/output.txt
FFMPEG it all together

python /gentle/align.py /tmp/output.mp3 /tmp/output.txt -o output.srt

Continue to remove hardcoded variables and replace with project/config/system vars
Create Reddit post ID storage (read/write from text file?)
Choose Reddit post that is not in ID storage (just go down the list from the top)
Create workdir that gets cleaned between outputs
Get a better run/build command - this is not good: go run src/main.go src/srt_generator.go src/reddit.go src/tts.go src/ffmpeg.go
Create creds reader and publisher for IG/TT/YT
