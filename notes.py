import numpy as np

middle_la = 440  # Hz
middle_la_offset = 9  # Distance from the C key of the middle octave

octave_weights = 2 ** (np.arange(12) / 12)
print(octave_weights)

print(440 * octave_weights)

middle_do = middle_la / octave_weights[middle_la_offset]
middle_octave = middle_do * octave_weights
print(middle_octave)

middle_la_distances = np.arange(-middle_la_offset, 12-middle_la_offset)
middle_octave_2 = middle_la *  2 ** (middle_la_distances / 12)
print(middle_octave_2)
