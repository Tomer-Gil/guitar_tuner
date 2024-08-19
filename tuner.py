import numpy as np

import helper_functions

CONCERT_PITCH = 440  # Hz
ALL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def find_closest_note(pitch):
    i = int(np.round(np.log2(pitch / CONCERT_PITCH) * 12))
    closest_pitch = CONCERT_PITCH * 2 ** (i / 12)
    closest_note = ALL_NOTES[i % 12] + str(4 + (i + 9) // 12)
    return closest_note, closest_pitch


def test_find_closest_note():
    print(find_closest_note(440))
    print(find_closest_note(880))
    print(find_closest_note(220))
    print(find_closest_note(210))


def main():
    helper_functions.record()
    helper_functions.plot()


if __name__ == "__main__":
    main()
