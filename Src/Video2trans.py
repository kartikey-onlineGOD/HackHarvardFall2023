from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
import moviepy.editor as mp

def extract_audio(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio_text = ""

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        audio_text = recognizer.recognize_google(audio)

    return audio_text

def generate_transcript_with_timestamps(video_path, output_transcript_path):
    extract_audio(video_path, "temp_audio.wav")
    audio_text = transcribe_audio("temp_audio.wav")
    video = mp.VideoFileClip(video_path)
    audio_duration = audio_file.duration

    # Calculate the time per transcript chunk (adjust as needed)
    time_per_chunk = 5  # in seconds

    with open(output_transcript_path, 'w') as transcript_file:
        for i in range(0, int(audio_duration), time_per_chunk):
            start_time = i
            end_time = min(i + time_per_chunk, audio_duration)
            chunk = audio_text[start_time:end_time]
            transcript_file.write(f"Time: {start_time} - {end_time}\n{chunk}\n\n")

if __name__ == '__main__':
    video_path = 'your_video.mp4'
    output_transcript_path = 'output_transcript.txt'
    
    generate_transcript_with_timestamps(video_path, output_transcript_path)
