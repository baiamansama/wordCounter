import operator
text = open("sample.txt", "r")

d = dict()
#f = open("output.txt", "a")
f = open("output.txt", "w")
writer = csv.writer(f)
f.truncate(0)
#follow the pattern and add words with lowercase
bad_list=["a","i", "to", "the", "an", "of", "from","and", "you", "no", "are", "am","not","but","we","he","she","from","do","they","was"]
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
      if word.isascii() or "’" in word:
        
        if word not in bad_list:
          if "’" or "." "?" or "!" in word:
            if "’" in word:
              arr = word.split("’")
            elif "." in word:
              arr = word.split(".")
            elif "!" in word:
              arr = word.split("!")
            word = arr[0]
            if word in d:
                d[word] = d[word] + 1
            else:
                print(word)
                d[word] = 1
          if word.isalpha():
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
          else:
            continue
        else:
          continue
      else:
        continue
print(d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
for key in list(sorted_d.keys()):
  writer.writerow([key, sorted_d[key]])
f.close()
print(d)