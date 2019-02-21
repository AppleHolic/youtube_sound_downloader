import os
import autoarg
import subprocess


def __main(youtube_url, output_path, format='pcm_f32le'):
    # get youtube url
    result = subprocess.run(['youtube-dl', '-g', youtube_url], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    sound_url = result.split('\n')[1]

    # sound download url
    os.system('ffmpeg -i \'{}\' -c copy -c:a {} {}'.format(sound_url, format, output_path))


def main():
    autoarg.run(__main)


if __name__ == '__main__':
    main()
