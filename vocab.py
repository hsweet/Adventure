
pronouns = ['I', 'you', 'he', 'she', 'we', 'they', 'it']

adjectives = [
    "good", "great", "big", "small", "beautiful", "ugly", "happy", "sad",
    "funny", "serious", "smart", "dumb", "hard", "easy", "fast", "slow",
    "nice", "mean", "kind", "cruel", "brave", "fearful", "tall", "short",
    "rich", "poor", "young", "old", "healthy", "sick"
]

sorted_adjectives = sorted(adjectives)

synonims = {
  # Any word in the lists could run the action. 
  # Better to say "open door" than "take door".  
  'use': ('open', 'close', 'hit', 'kick', 'hug'),
  'take': ('get', 'pick', 'grab')
}
          

ordinals = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth'
}

##### DO NOT EDIT THE CODE BELOW THIS LINE #####

def plural(word):
  '''add s if, es if etc'''
  pass


def article(word):
  '''should we use an a or an before an object?'''
  vowels = ('a', 'e', 'i', 'o', 'u')
  if word[0].lower() in vowels:
    return 'an ' + word
  else:
    return 'a ' + word


def ordinal(number):
  if number in ordinals:
    return ordinals[number]
  elif type(number) == int:
    return number
  else:
    return 0  # error, input not a number

if __name__ == '__main__':
  print(ordinal(4))
  print(article('Attract'))
