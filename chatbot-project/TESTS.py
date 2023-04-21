from mtranslate import translate
from langdetect import detect
import langid

languagesPrefixes= [
  {
    "prefix": "af",
    "name": "Afrikaans"
  },
  {
    "prefix": "sq",
    "name": "Albanian"
  },
  {
    "prefix": "am",
    "name": "Amharic"
  },
  {
    "prefix": "ar",
    "name": "Arabic"
  },
  {
    "prefix": "hy",
    "name": "Armenian"
  },
  {
    "prefix": "az",
    "name": "Azerbaijani"
  },
  {
    "prefix": "eu",
    "name": "Basque"
  },
  {
    "prefix": "be",
    "name": "Belarusian"
  },
  {
    "prefix": "bn",
    "name": "Bengali"
  },
  {
    "prefix": "bs",
    "name": "Bosnian"
  },
  {
    "prefix": "bg",
    "name": "Bulgarian"
  },
  {
    "prefix": "ca",
    "name": "Catalan"
  },
  {
    "prefix": "ceb",
    "name": "Cebuano"
  },
  {
    "prefix": "ny",
    "name": "Chichewa"
  },
  {
    "prefix": "zh-cn",
    "name": "Chinese (Simplified)"
  },
  {
    "prefix": "zh-tw",
    "name": "Chinese (Traditional)"
  },
  {
    "prefix": "co",
    "name": "Corsican"
  },
  {
    "prefix": "hr",
    "name": "Croatian"
  },
  {
    "prefix": "cs",
    "name": "Czech"
  },
  {
    "prefix": "da",
    "name": "Danish"
  },
  {
    "prefix": "nl",
    "name": "Dutch"
  },
  {
    "prefix": "en",
    "name": "English"
  },
  {
    "prefix": "eo",
    "name": "Esperanto"
  },
  {
    "prefix": "et",
    "name": "Estonian"
  },
  {
    "prefix": "tl",
    "name": "Filipino"
  },
  {
    "prefix": "fi",
    "name": "Finnish"
  },
  {
    "prefix": "fr",
    "name": "French"
  },
  {
    "prefix": "fy",
    "name": "Frisian"
  },
  {
    "prefix": "gl",
    "name": "Galician"
  },
  {
    "prefix": "ka",
    "name": "Georgian"
  },
  {
    "prefix": "de",
    "name": "German"
  },
  {
    "prefix": "el",
    "name": "Greek"
  },
  {
    "prefix": "gu",
    "name": "Gujarati"
  },
  {
    "prefix": "ht",
    "name": "Haitian Creole"
  },
  {
    "prefix": "ha",
    "name": "Hausa"
  },
  {
    "prefix": "haw",
    "name": "Hawaiian"
  },
  {
    "prefix": "iw",
    "name": "Hebrew"
  },
  {
    "prefix": "he",
    "name": "Hebrew"
  },
  {
    "prefix": "hi",
    "name": "Hindi"
  },
  {
    "prefix": "hmn",
    "name": "Hmong"
  },
  {
    "prefix": "hu",
    "name": "Hungarian"
  },
  {
    "prefix": "is",
    "name": "Icelandic"
  },
  {
    "prefix": "ig",
    "name": "Igbo"
  },
  {
    "prefix": "id",
    "name": "Indonesian"
  },
  {
    "prefix": "ga",
    "name": "Irish"
  },
  {
    "prefix": "it",
    "name": "Italian"
  },
  {
    "prefix": "ja",
    "name": "Japanese"
  },
  {
    "prefix": "jw",
    "name": "Javanese"
  },
  {
    "prefix": "kn",
    "name": "Kannada"
  },
  {
    "prefix": "kk",
    "name": "Kazakh"
  },
  {
    "prefix": "km",
    "name": "Khmer"
  },
  {
    "prefix": "rw",
    "name": "Kinyarwanda"
  },
  {
    "prefix": "ko",
    "name": "Korean"
  },
  {
    "prefix": "ku",
    "name": "Kurdish (Kurmanji)"
  },
  {
    "prefix": "ky",
    "name": "Kyrgyz"
  },
  {
    "prefix": "lo",
    "name": "Lao"
  },
  {
    "prefix": "la",
    "name": "Latin"
  },
  {
    "prefix": "lv",
    "name": "Latvian"
  },
  {
    "prefix": "lt",
    "name": "Lithuanian"
  },
  {
    "prefix": "lb",
    "name": "Luxembourgish"
  },
  {
    "prefix": "mk",
    "name": "Macedonian"
  },
  {
    "prefix": "mg",
    "name": "Malagasy"
  },
  {
    "prefix": "ms",
    "name": "Malay"
  },
  {
    "prefix": "ml",
    "name": "Malayalam"
  },
  {
    "prefix": "mt",
    "name": "Maltese"
  },
  {
    "prefix": "mi",
    "name": "Maori"
  },
  {
    "prefix": "mr",
    "name": "Marathi"
  },
  {
    "prefix": "mn",
    "name": "Mongolian"
  },
  {
    "prefix": "my",
    "name": "Myanmar (Burmese)"
  },
  {
    "prefix": "ne",
    "name": "Nepali"
  },
  {
    "prefix": "no",
    "name": "Norwegian"
  },
  {
    "prefix": "or",
    "name": "Odia"
  },
  {
    "prefix": "ps",
    "name": "Pashto"
  },
  {
    "prefix": "fa",
    "name": "Persian"
  },
  {
    "prefix": "pl",
    "name": "Polish"
  },
  {
    "prefix": "pt",
    "name": "Portuguese"
  },
  {
    "prefix": "pa",
    "name": "Punjabi"
  },
  {
    "prefix": "ro",
    "name": "Romanian"
  },
  {
    "prefix": "ru",
    "name": "Russian"
  },
  {
    "prefix": "sm",
    "name": "Samoan"
  },
  {
    "prefix": "gd",
    "name": "Scots Gaelic"
  },
  {
    "prefix": "sr",
    "name": "Serbian"
  },
  {
    "prefix": "st",
    "name": "Sesotho"
  },
  {
    "prefix": "sn",
    "name": "Shona"
  },
  {
    "prefix": "sd",
    "name": "Sindhi"
  },
  {
    "prefix": "si",
    "name": "Sinhala"
  },
  {
    "prefix": "sk",
    "name": "Slovak"
  },
  {
    "prefix": "sl",
    "name": "Slovenian"
  },
  {
    "prefix": "so",
    "name": "Somali"
  },
  {
    "prefix": "es",
    "name": "Spanish"
  },
  {
    "prefix": "su",
    "name": "Sundanese"
  },
  {
    "prefix": "sw",
    "name": "Swahili"
  },
  {
    "prefix": "sv",
    "name": "Swedish"
  },
  {
    "prefix": "tg",
    "name": "Tajik"
  },
  {
    "prefix": "ta",
    "name": "Tamil"
  },
  {
    "prefix": "tt",
    "name": "Tatar"
  },
  {
    "prefix": "te",
    "name": "Telugu"
  },
  {
    "prefix": "th",
    "name": "Thai"
  },
  {
    "prefix": "tr",
    "name": "Turkish"
  },
  {
    "prefix": "tk",
    "name": "Turkmen"
  },
  {
    "prefix": "uk",
    "name": "Ukrainian"
  },
  {
    "prefix": "ur",
    "name": "Urdu"
  },
  {
    "prefix": "ug",
    "name": "Uyghur"
  },
  {
    "prefix": "uz",
    "name": "Uzbek"
  },
  {
    "prefix": "vi",
    "name": "Vietnamese"
  },
  {
    "prefix": "cy",
    "name": "Welsh"
  },
  {
    "prefix": "xh",
    "name": "Xhosa"
  },
  {
    "prefix": "yi",
    "name": "Yiddish"
  },
  {
    "prefix": "yo",
    "name": "Yoruba"
  },
  {
    "prefix": "zu",
    "name": "Zulu"
  }
]

# Define a function to handle user input
def handle_user_input(input_text):
    # Check if the input text contains any English words
    if all(langid.classify(word)[0] == 'en' for word in input_text.split()):
        return 'English', 'en'
    elif all(langid.classify(word)[0] == 'es' for word in input_text.split()):
        return 'Spanish', 'es'
    elif all(langid.classify(word)[0] == 'fr' for word in input_text.split()):
        return 'French', 'fr'
    else:
        # Detect the language of the input text
        lang, confidence = langid.classify(input_text)
        return lang, lang[:2]
        

# Take user input and handle it
while True:
    
    input_text = input("Enter text to translate: ")
    language, prefix = handle_user_input(input_text)
    
    if prefix != 'en':
        englishText = translate(input_text, 'en')
    else:
        englishText = input_text
    for l in languagesPrefixes:
      if l["prefix"] == prefix:
          language = l["name"]
    
    print(f"Language was: {language}, and In English is:")
    print(englishText)
