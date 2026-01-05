# API Request

**Endpoint:** `POST /evaluate`
**Content-Type:** `multipart/form-data`

## Parameters

| Parameter | Type | Required | Description | Default |
| :--- | :--- | :--- | :--- | :--- |
| `file` | File | Yes | The audio file containing the speech to evaluate (e.g., .wav, .mp3). | - |
| `text` | String | Yes | The target word or phrase that the audio attempts to speak. | - |
| `language` | String | No | The language code for evaluation (e.g., `en-us`, `en-gb`). | `en-us` |

# API Response Structure

The `POST /evaluate` endpoint returns a JSON object with the following structure:

```json
{
  "overall_score": 85,
  "words": [
    {
      "word": "apple",
      "quality_score": 90,
      "start_time": 0.5,
      "end_time": 1.2,
      "syllables": [
        {
          "syllable": "ap",
          "quality_score": 95,
          "start_time": 0.5,
          "end_time": 0.8
        },
        {
          "syllable": "ple",
          "quality_score": 85,
          "start_time": 0.8,
          "end_time": 1.2
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
  - **start_time** (float): Start time of the word in seconds.
  - **end_time** (float): End time of the word in seconds.
  - **syllables** (list): A breakdown of the word into syllables/phonemes.
    - **syllable** (string): The letters corresponding to the syllable/phoneme.
    - **quality_score** (int): The quality score for this syllable (0-100).
    - **start_time** (float): Start time of the syllable in seconds.
    - **end_time** (float): End time of the syllable in seconds.
