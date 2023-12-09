import json
import os

CONF_FILE = 'conf.json'


class Conf:
  defaults = {
    "distance": 40,
    "angle": 25,
    "graph_k": 3,
    "graph_max_iter": 1,
    "graph_percent_to_keep": 0.8,
    "radius": 18,
    "radius_min_connections": 3,
    "radius_max_iter": 5
  }

  default_max = 100

  max = {
    'angle': 180,
    'graph_max_iter': 5,
    'graph_percent_to_keep': 100,
    'radius_max_iter': 5,
    'radius_min_connections': 10,
  }

  decimal_keys = ['graph_percent_to_keep']

  def __init__(self):
    if os.path.isfile(CONF_FILE):
      with open(CONF_FILE, 'r') as f:
        self.conf = json.load(f)
    else:
      self.conf = {}

  def get(self, img, key):
    if img not in self.conf:
      self.conf[img] = self.defaults.copy()

    if key in self.decimal_keys:
      return round(self.conf[img][key] * 100)
    else:
      return self.conf[img][key]

  def get_img_conf(self, img):
    if img not in self.conf:
      self.conf[img] = self.defaults.copy()
    return self.conf[img]

  def set(self, img, key, val):
    if val <= 0:
      self.conf[img][key] = 1
    else:
      val = min(self.max_val(key), val)
      if key in self.decimal_keys:
        self.conf[img][key] = round(val / 100, 2)
      else:
        self.conf[img][key] = val

  def max_val(self, key):
    return self.max.get(key, self.default_max)

  def keys(self):
    return self.defaults.keys()

  def save(self):
    with open(CONF_FILE, 'w+') as f:
      f.write(json.dumps(self.conf, indent=2))
