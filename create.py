import json, names, random

def random_values():
  keys = ["citizen","residence","gender","age","edu","army",
  "religion","church","language","gredu","gruniv","secstate",
  "awaytime","grtime","assets","tax","voted","rightvote",
  "wantvote","willvote","issues"]
  values = {}
  for x in xrange(0,21):
    values["name"] = names.get_first_name() # actually it's responder id
    if x == 0 or x == 2 or x == 10 or x == 15 or x == 16:
      values[keys[x]] = random.choice([True, False])
    elif x == 1:
      values[keys[x]] = random.choice(["US", "DE", "UK", "AT", "AU", "IT"])
    elif x == 20:
      values[keys[x]] = random.sample(set([0, 1, 2, 3, 4, 5]), 3)
    else:
      values[keys[x]] = random.choice([0, 1, 2, 3, 4])

  return values

def random_data():
  d = []
  for x in xrange(1,30):
    d.append(random_values())

  return d

def create_json(debug=True):
  with open("data.json", "w") as file:
    if debug == True:
      json.dump(random_data(), file, indent=2)
    else:
      json.dump(data, file, indent=2)

if __name__ == '__main__':
  create_json()
