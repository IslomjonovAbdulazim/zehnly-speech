# API Response Structure

The `POST /evaluate` endpoint returns a JSON object with the following structure:

```json
{
  "overall_score": 85,
  "words": [
    {
      "word": "apple",
      "quality_score": 90,
      "syllables": [
        {
          "syllable": "ap",
          "quality_score": 95
        },
        {
          "syllable": "ple",
          "quality_score": 85
        }
      ]
    }
  ]
}
```

## Fields

- **overall_score** (int): The overall quality score of the speech (0-100).
- **words** (list): A list of word objects analyzed in the audio.
  - **word** (string): The word text.
  - **quality_score** (int): The quality score for this specific word (0-100).
  - **syllables** (list): A breakdown of the word into syllables/phonemes.
    - **syllable** (string): The letters corresponding to the syllable/phoneme.
    - **quality_score** (int): The quality score for this syllable (0-100).
