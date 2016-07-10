
# TODO - Turn this into something that runs with unit tests or something?

import timeit

from edit_distance import edit_distance_backpointer
from edit_distance import edit_distance
from edit_distance import highest_match_action
from edit_distance import SequenceMatcher

# TODO - Benchmark the other primary functions (e.g. with and without backpointers)

a = ['a', 'b'] * 5
b = ['a', 'c', 'd', 'a', 'b'] * 5

setup_string = "from edit_distance import edit_distance_backpointer; a = {}; b = {}".format(a, b)
run_string = 'edit_distance_backpointer(a, b)'
t = timeit.Timer(run_string, setup=setup_string)
n = 1000
total_time = t.timeit(number=1000)
avg_time = total_time / n;  # in seconds
print('Average time: {:.2f} ms'.format(avg_time * 1000))