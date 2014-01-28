import sys
import urllib
import urllib2
from subprocess import call

google_translate = "http://translate.google.com/translate_tts?"

def url_construct(text):
    """Constructs the url for the HTTP request to Google Translate"""
    language = { "tl": "en-us" }
    text = { "q": text }
    encoding = { "ie": "utf-8" }

    url = google_translate + urllib.urlencode(encoding) + "&" + \
                             urllib.urlencode(text) + "&" + \
                             urllib.urlencode(language)

    return url

def mp3_file_create(data):
    """Creates a temporary mp3 file"""
    mp3_file = open("speech.mp3", "wb")
    mp3_file.write(data)
    mp3_file.close()

    return "speech.mp3"

def text_to_speech(text):
    """Converts passed text to speech"""
    url = url_construct(text)
    request = urllib2.Request(url, headers = { "User-Agent": "Firefox" })

    data = urllib2.urlopen(request).read()
    path = mp3_file_create(data)
    call(["open", path])

def main():
    word_count = len(sys.argv)
    text_to_speech(sys.argv[1:word_count])

if __name__ == "__main__":
    main()
