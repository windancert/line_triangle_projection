import cProfile
import line_2d3d

cProfile.run('line_2d3d.main()', 'profile.dat')

import pstats

with open("profile_time.txt", "w") as f:
     p = pstats.Stats('profile.dat', stream=f)
     p.sort_stats("time").print_stats()

with open("profile_calls.txt", "w") as f:
     p = pstats.Stats('profile.dat', stream=f)
     p.sort_stats("calls").print_stats()

