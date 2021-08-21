input = "abadabace"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for c in string:
      if c.isalpha() :
        alphabet_occurrence_array[ord(c)-ord('a')] += 1

    not_repeat_character_array = []
    for index in range(len(alphabet_occurrence_array)):
      alphabet_occurrence = alphabet_occurrence_array[index]
      if alphabet_occurrence == 1:
        not_repeat_character_array.append(chr(index+ord('a')))
    
    for c in string:
      if c in not_repeat_character_array:
        return c

result = find_not_repeating_character(input)
print(result)