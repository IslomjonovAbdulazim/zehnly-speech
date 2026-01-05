import os
import requests
from dotenv import load_dotenv

load_dotenv()

SPEECHACE_KEY = os.getenv("SPEECHACE_KEY")
SPEECHACE_API = os.getenv("SPEECHACE_API", "https://api5.speechace.com")

def evaluate_speech(audio_file, text, language="en-us", user_id="test-user"):
    url = f"{SPEECHACE_API}/api/scoring/text/v9/json"
    
    params = {
        "key": SPEECHACE_KEY
    }

    data = {
        "dialect": language,
        "user_id": user_id,
        "text": text,
    }
    
    files = {
        "user_audio_file": ("audio.wav", audio_file, "audio/wav")
    }
    
    try:
        response = requests.post(url, params=params, data=data, files=files)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling SpeechAce API: {e}")
        if e.response is not None:
             print(f"Response content: {e.response.text}")
        return None

def format_speechace_response(raw_response):
    if not raw_response:
         return {"error": "No response from SpeechAce"}
         
    if "text_score" not in raw_response:
        # Return the whole response if unexpected structure, for debugging/info
        return {"error": "Could not score audio", "details": raw_response}

    text_score = raw_response["text_score"]
    word_score_list = text_score.get("word_score_list", [])
    
    formatted_words = []
    
    for word_data in word_score_list:
        word = word_data.get("word")
        quality_score = word_data.get("quality_score")
        
        syllable_score_list = word_data.get("syllable_score_list", [])
        formatted_syllables = []
        
        for syllable_data in syllable_score_list:
            formatted_syllables.append({
                "syllable": syllable_data.get("letters"),
                "quality_score": syllable_data.get("quality_score")
            })

        formatted_words.append({
            "word": word,
            "quality_score": quality_score,
            "syllables": formatted_syllables
        })

    return {
        "overall_score": text_score.get("quality_score"),
        "words": formatted_words
    }
