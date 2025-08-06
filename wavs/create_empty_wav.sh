# $1 - length in seconds
ffmpeg -f lavfi -i anullsrc -t $1 -f wav -bitexact -acodec pcm_s16le -ar 44100 -ac 1
