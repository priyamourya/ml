from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
import pickle

summarizer = pipeline('summarization')
pkl_file= open('file.pkl', 'wb')
pickle.dump(summarizer,pkl_file)
pkl_file.close()
