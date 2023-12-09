import cv2
from matplotlib import pyplot as plt
from position_utils import *
from scipy.spatial import distance
import math
import numpy as np


class bottom_up:
  def __init__(self):
    return

  def angle(self, x1, y1, x2, y2):
    angle = math.degrees(math.atan2((y2 - y1), (x2 - x1)))
    return angle

  def angle_diff(self, a1, a2):
    diff = np.abs(a1 - a2)
    return diff

  def get_distance_angle(self, dots):
    x, y = find_dot_centres(dots)
    self.x_coords, self.y_coords = x.copy(), y.copy()
    self.no_dots = len(x)
    dists = np.zeros((self.no_dots, self.no_dots))
    angles = np.zeros((self.no_dots, self.no_dots))
    for i in range(self.no_dots):
      for j in range(self.no_dots):
        dists[i, j] = distance.euclidean((x[i], y[i]), (x[j], y[j]))
        angles[i, j] = self.angle(x[i], y[i], x[j], y[j])
    return dists, angles

  def threshold_angle_on_distance(self, angles, dists, threshold=25):
    mask = (dists > threshold) | (dists == 0)
    mask_inds = np.where(mask)
    angles[mask_inds[0], mask_inds[1]] = np.nan
    return angles

  def get_connection_table_angle_thresholded(self, angles, a_tolerance=5):
    '''angle thresholding a_tolerance in angles table where i,j defines the line segment and the value in angles gives its absolute angle'''
    d_max = 180 + a_tolerance
    d_min = 180 - a_tolerance
    conn = np.ones((self.no_dots, self.no_dots)) * -1
    dia = np.diag(np.zeros(self.no_dots))
    for i in range(self.no_dots):
      temp = angles[i, :]
      diff = self.angle_diff(np.expand_dims(angles[i, :], axis=1), np.expand_dims(angles[i, :], axis=0))
      diff += dia
      ind = np.where((d_min < diff) & (diff < d_max))
      conn[i, ind[0]] = ind[1]
    return conn

  def filter_long_lines(self, conn, sequence_threshold=6):
    connections = []
    # scan for connections
    for j in range(self.no_dots):
      pt = np.where(conn[:, j] > 0)
      for st in pt[0]:
        candidate = []
        btw = int(st)
        nxt = int(conn[btw, j])
        prev = j
        candidate.append(prev)
        candidate.append(btw)
        while (nxt > 0 and nxt not in candidate):
          candidate.append(nxt)
          prev = btw
          btw = nxt
          nxt = int(conn[btw, prev])
        # reverse check
        prev = candidate[1]
        btw = candidate[0]
        nxt = int(conn[btw, prev])
        while (nxt > 0 and nxt not in candidate):
          candidate.insert(0, nxt)
          prev = btw
          btw = nxt
          nxt = int(conn[btw, prev])
        if (len(candidate) > sequence_threshold):
          connections.append(candidate)
    return connections

  def compare_sequences(self, a, b):
    lens = [len(a), len(b)]
    seqs = [a, b]
    s_inds = np.argsort(lens)
    ref_seq = seqs[s_inds[0]]
    search_seq = seqs[s_inds[1]]
    i = 0
    while (i < len(search_seq)):
      for j in range(len(ref_seq)):
        if (i >= len(search_seq)):
          break
        if ((search_seq[i] == ref_seq[j])):
          i += 1
          continue
        else:
          i += 1
          break
      if (j == len(ref_seq) - 1):
        return s_inds[0]
    ref_seq = np.flip(ref_seq)
    i = 0
    while (i < len(search_seq)):
      for j in range(len(ref_seq)):
        if (i >= len(search_seq)):
          break
        if ((search_seq[i] == ref_seq[j])):
          i += 1
          continue
        else:
          i += 1
          break
      if (j == len(ref_seq) - 1):
        return s_inds[0]
    return -1

  def clean_same_sequences(self, seq):
    seqs = seq.copy()
    i = 0
    while (i < len(seqs) - 1):
      j = i + 1
      while (j < len(seqs) - 1):
        c = self.compare_sequences(seqs[i], seqs[j])
        if (c == 0):
          del [seqs[i]]
        elif (c == 1):
          del [seqs[j]]
        else:
          j += 1
      i += 1
    return seqs

  def index_to_seqs(self, seqs):
    ''' Changes the sequence from dot index to the x,y point in pixel space'''
    coord_seqs = []
    for seq in seqs:
      coord_seqs.append(np.stack((self.x_coords[seq], self.y_coords[seq]), axis=1).astype(int))
    return coord_seqs

  def find_sequence(self, image, distance=25, angle=10):
    ''' Function expected to be called, give it an image and expect in return sequence of co-ordinates of dots connected by bottom-up bias curves'''
    self.dots = stimuli_dots(image)
    dists, angles = self.get_distance_angle(self.dots)
    angles = self.threshold_angle_on_distance(angles, dists, threshold=distance)
    conn = self.get_connection_table_angle_thresholded(angles, a_tolerance=angle)
    connections = self.filter_long_lines(conn, sequence_threshold=5)
    final_seqs = self.clean_same_sequences(connections)
    final_coord_seqs = self.index_to_seqs(final_seqs)
    return final_coord_seqs
