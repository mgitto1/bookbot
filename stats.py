def get_book_text(path):
  with open(path) as f:
    return(f'Found {len(f.read().split())} total words')

def get_count_char(path):
  with open(path) as f:
    dict = {}
    for l in f.read():
      letter = l.lower()
      if letter in dict:
        dict[letter] += 1
      else:
        dict[letter] = 1
    return dict

def return_sorted_dict(dictionary):
  sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
  return(sorted_dict)

def iterate_dict(dict):
  str = ''
  for letter in dict:
    str += f'{letter}: {dict[letter]}\n'
  return str

def print_report(path):
  count_string = get_book_text(path)
  sorted_dict = get_count_char(path)

  print(f'============ BOOKBOT ============\n'
      f'Analyzing book found at {path}...\n'
      f'----------- Word Count ----------\n'
      f'{count_string}\n'
      f'--------- Character Count -------\n'
      f'{iterate_dict(sorted_dict)}\n'
      f'============= END ==============='
  )


