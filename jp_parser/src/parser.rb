require 've'

# Parse a string of Japanese text into an array of its components.
#
# Currently extracts:
#   - Original word as found in text.
#   - Lemma (base word of inflected words).
#   - Part of Speech
#   - Reading (Katakana)
#
# TODO: Handle inflection types better.
def parse_jp(text)
  words = Ve.in(:ja).words(text)


  # TODO: When adding inflection support:
  # Ve provides a word.inflected? method.
  filtered_words = words.map do |word|
    { 
      word: word.word, 
      lemma: word.lemma, 
      part_of_speech: word.part_of_speech.name, 
      reading: word.extra[:reading] 
    } 
  end
end
