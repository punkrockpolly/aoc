from collections import defaultdict, deque


DAY_20_INPUT = """                                         J       F           Z     S   X           H     T                                             
                                         Q       V           V     K   P           K     D                                             
  #######################################.#######.###########.#####.###.###########.#####.###########################################  
  #...#...#.#...........#.#.....#.#.....#...#.#.#.....#.#...#...#...#.#...#.........#.#...................#.#.#.#...#.#.....#.......#  
  ###.###.#.#######.#####.#.#.#.#.###.#.###.#.#.#.###.#.###.#.#####.#.#.#.#######.###.#.#.#.###.###.#.###.#.#.#.###.#.###.#.###.###.#  
  #.#.....#.#.#.#.#...#.#...#.#.....#.#.....#.......#.#.........#...#...#.#.....#.....#.#.#.#.#...#.#.#.#.......#...#.....#.#.....#.#  
  #.#####.#.#.#.#.#.###.#########.#.###.#.#####.#######.#.#########.###.#####.#.#####.#.#####.#########.#.#######.#.###.#####.#.#.#.#  
  #.#...#.....#...#...#.....#...#.#.....#.#.#.......#...#.#...#.....#.#.......#.#.....#.#...........#...#.#.#.....#.#.......#.#.#.#.#  
  #.###.#.###.###.###.###.###.#####.###.###.###.#########.#.#.#.#.###.#######.#####.###.#.#.###########.###.#.#######.###.###.#####.#  
  #...#.#.#.#...#.#.....#...#.........#.....#.#...#.........#.#.#.....#.........#.#.#.#...#...#...#.......#.....#...#.#.#.#.#.#.#.#.#  
  ###.#.###.###.#.###.###.###############.###.#.###.#.###.###.#######.#.###.#####.#.#.#.#.###.#.#######.###.#####.###.#.###.#.#.#.###  
  #.#.................#.#.#...#...#.........#...#.#.#.#...#.....#.#...#.#.....#.#.....#.#.#.......#.#.......#.....#.#.#.............#  
  #.#################.#.#.###.#.#####.#.###.###.#.###.#.#.###.###.#.###.#######.#.###.#####.#######.###.###.###.###.#.#.###.###.#####  
  #.#...#...#...#.#...............#.#.#.#...#.......#.#.#...#.#.......#.......#...#...#...#...............#.......#.......#.#.....#.#  
  #.###.#.#####.#.#.#####.#####.###.#####.#####.#.###########.###.#.#.#.#######.###.#.#.#.###.#####.###.#########.###.#.###########.#  
  #...#.....#.#.....#...#.#.#.#.............#...#.#.#...#.#...#...#.#.#.#...#...#...#.#.#.........#...#.....#...#.#...#...#.#.#.#...#  
  #.###.###.#.#####.###.#.#.#.###.#######.#.###.###.###.#.###.###.###.#.#.#########.#.###.#.###.###.#####.###.#######.#####.#.#.###.#  
  #...#...#.#.#...#.#.....#.............#.#...#.......#...#.....#.#...#.....#...#.#.#.#...#.#.....#.....#.....#.....#.#.#...#.#.....#  
  ###.#.#####.###.###.#.#.###.#.#.#######.###.###.###.#.#.###.#.#####.###.###.###.#.#.#.#######.###.#.###########.###.#.###.#.###.###  
  #.#...#.#...........#.#.#...#.#.#...#...#...#.#...#.#.#.....#.#.#...#...........#.#.#...#.#.....#.#.....#.#...#.#.....#.#...#.#...#  
  #.#.###.#.#####.#.#.###.#########.#####.###.#.#.###########.###.###.#.#.#.###.#####.#.###.###########.###.###.#.###.###.#.###.#.###  
  #.#.....#.#.....#.#.#.......#.....#...#.#...#.....#.....#.#.....#...#.#.#...#.....#.#.#.#...#...#.#.....#.#.......#.........#.#.#.#  
  #.#.###########################.#####.###.#.#.#########.#.#.#######.#.#######.#.###.#.#.#.###.#.#.#.#.###.###.#####.#.###.###.#.#.#  
  #.....#.....#.#...#.....#.#...#.....#.#.#.#.#...#...#.#...#...#.....#.....#.#.#.#...#...#.....#...#.#.#.....#.#.#.#.#...#.#.#.....#  
  #.#.###.#####.#.#.#####.#.###.###.###.#.###.#.###.###.#.#.#.#######.#.#.###.#.#####.###.#.###############.###.#.#.###.#####.###.###  
  #.#.....#...#...#.....#.#.....#...#.#...#...#.......#...#...#.......#.#.#.#...#...#.#.....#.#.#.....#.#.................#...#.#...#  
  ###.#######.#####.#.#.#.#####.#.#.#.###.###.#.#.###.#.#######.###.###.###.###.#.#.#.#.#.###.#.###.###.#######.###.#####.###.#.#.###  
  #...#.#.#...#.#.#.#.#.....#.#.#.#...#.....#.#.#...#.#.....#.#.#...#.....#...#.#.#...#.#.#.#.......#.....#.#.....#.....#.#.....#.#.#  
  #.#.#.#.#.###.#.#########.#.#.#####.###.###.#.#.###.#.#.#.#.#####.###.#.###.#####.###.###.#.###.#.###.#.#.###.#############.###.#.#  
  #.#.#.#...#.#.#.....#.............#.#.....#.#.#.#...#.#.#.....#.....#.#.....#...#...#...#.#.#.#.#...#.#.#...#.#...#.#...#.....#...#  
  #.###.#.###.#.###.#####.###.#####.#.#####.#.###.###.#######.#######.###.###.###.###.#.###.#.#.###.#####.###.#.###.#.###.###.###.#.#  
  #...#.....#...#.#.....#.#.#...#.#.............#.#.....#...#.....#.#...#.#...#...#...#.......#...#.#.#...#.....#.#...#.....#...#.#.#  
  #.#######.###.#.###.#####.#####.#####.#.###.###.###.#####.#.#####.#.#######.#.#.#.#####.###.#.#####.###.#.#####.###.###.#####.###.#  
  #...#.#.....#.....#...#...#...#.#.....#.#...#.#.#...#.......#...#.#...#.....#.#.#...#...#...#...#...#.#.....#.#.#.#.#...#...#...#.#  
  #.###.###.###.#######.#.#####.#.###########.#.#.###.#.###.###.#.#.#.#######.#.#.###.###.#.###.###.###.#.###.#.#.#.#.###.#.###.###.#  
  #.#.#.............#.#...#.#.#...#.#...........#.#...#...#...#.#.........#...#.#.......#.#.......#.........#.....#.#...#...........#  
  #.#.#.#####.#.#.#.#.#.#.#.#.#.###.#####.#########.#####.#####.###########.###.#############.#######.#.###########.###.#######.#.###  
  #...#.#...#.#.#.#.#...#.#.#...#...#    J         R     L     Y           L   I             X    #.#.#.#.#.#.#...#.#...#.....#.#.#.#  
  #.###.#.###########.#####.###.#.###    N         P     P     L           S   B             P    #.###.#.#.#.#.###.#.#######.#.###.#  
  #...#.#...........#.#.#.#...#...#.#                                                             #.#.....#.........#.....#.#...#.#..AA
  #.###.#.#.#########.#.#.###.#.###.#                                                             #.###.#.#.#.###.#.#.###.#.###.#.#.#  
YL..#.....#.#.#.#.#.#.#..............EK                                                           #.....#.#.#.#...#...#.......#.#....UT
  #.###.#.###.#.#.#.#.###.#####.###.#                                                             #.#####.#.#.#.###.###.#######.###.#  
  #.....#.......#.......#.#.#.#.#.#.#                                                           ZV..#...#.#.#.#...#...#.#.....#.....#  
  #####.###.###.#######.###.#.#.#.###                                                             #.#.###.#.###.#######.###.#.#.#.#.#  
  #.......#...#.#.........#.........#                                                             #.#.#.#.....#.#...#.......#...#.#.#  
  #########.#######.###.#.#.###.#####                                                             ###.#.#.#.#.#.#.#########.###.###.#  
  #.#...#...........#...#...#.#.#...#                                                             #.....#.#.#.#.#.........#...#.#.#.#  
  #.###.#####################.#####.#                                                             ###.#.#########.#.#.###.#######.###  
  #.............#...........#...#.#..YS                                                           #...#.#...#.#.#.#.#.#.........#...#  
  #####.###.###.#.#####.###.###.#.#.#                                                             #.#.#.#.###.#.#####.#####.#######.#  
  #.......#...#.......#...#.........#                                                           FV..#.#...#.....#...#...#...#...#...#  
  ###.#.#.#.#.#.#.###.#.###.###.###.#                                                             #####.#####.#.###.###.#.###.#.#.#.#  
JB..#.#.#.#.#.#.#...#.#.#.....#.#.#.#                                                             #...........#.........#.....#...#..ZP
  #.#.###########.#.###.#########.###                                                             #.#.#######################.#######  
ZZ....#.....#.#.#.#.#.....#.........#                                                             #.#.#.#...#.#.............#.#......IB
  #.#####.###.#.#######.###.###.#####                                                             #####.#.#.#.#.#.#.#.#####.###.#.#.#  
  #.#...........#.....#.#...#.#.....#                                                           QR......#.#.#...#.#.#...#.....#.#.#.#  
  ###.#.#####.#####.#########.#.###.#                                                             #####.#.#.#.#####.#########.#.###.#  
  #.#.#...#.#.....#.#.......#.....#.#                                                             #.#.....#.....#...#.#...#...#...#.#  
  #.#####.#.###.###.###.#####.#.#.#.#                                                             #.###.#.###.###.#.#.#.###.###.#####  
  #.#...#.....#...#.#.#.#.#.#.#.#.#..ZP                                                           #...#.#...#...#.#.#.#.#.......#.#.#  
  #.#.#.#####.#.###.#.#.#.#.#####.###                                                             #.#################.#.#.#.#####.#.#  
YS....#.......#...................#.#                                                           TD..#...#.....#.#...#.#.#.#.#.....#..ZJ
  #######.###.#########.###.#.###.#.#                                                             #.###.###.###.#.###.#.###.#.###.#.#  
EK......#.#.#...#.........#.#.#.....#                                                             #.......#...#.....#.#.#...#...#.#.#  
  #####.###.#####.#.#################                                                             ###.#.###.###.#.###.#.#######.#.#.#  
  #.....#.#.#...#.#.#.#.#.....#.#...#                                                             #...#.#.....#.#.#.....#.......#...#  
  ###.#.#.#.#.#######.#.#.###.#.#.###                                                             #####.###.###.#.###.#.###.#.#.#.#.#  
  #...#.#.......#.........#.#.#.#...#                                                             #.#.#.........#.....#.....#.#.#.#.#  
  ###.###.###.#.#####.###.#.#.#.#.###                                                             #.#.#######################.#######  
  #.#.......#.#.......#.#.#.#........QP                                                           #...#...#...........#.....#.#.....#  
  #.###########.#####.#.###.#########                                                             #.#.#.#.#.###.#####.#.#.#####.###.#  
MP........#...#...#...#.......#.....#                                                             #.#...#.....#.#.....#.#.....#...#.#  
  #######.#.#########.#.#####.#.###.#                                                             #.###.#.#.#.#.#####.#.#####.###.#.#  
  #.........#...#...#.#.#.....#...#..TV                                                         NU....#.#.#.#.#.#.........#.....#.#..RP
  #.###.#######.#.#####.###.#####.###                                                             #.###.###############.#######.#.###  
  #.#...#.......#.#.#...#...#.....#.#                                                             #.#.#...#...#.#...#.#.#...#.......#  
  #.#####.#.#####.#.#.#####.###.###.#                                                             ###.#.###.###.###.#.###.#####.#####  
  #.......#...........#...#.....#.#.#                                                           RX....#.#.#.#.....#.#.#...#.#...#....JN
  #######.#######.#.#.#.#########.#.#                                                             #.#####.#.#.#####.#.#.#.#.#######.#  
  #...#.......#...#.#.#.....#...#....MP                                                           #.#.#...#...#.........#.#.....#...#  
  #.###################.###.#.#.#.#.#                                                             #.#.###.###.#####.#.#.#####.#####.#  
OF..#...#...#...#.#.#.....#...#.#.#..NZ                                                           #.#.....#...#...#.#.#.#.#.#.#.#.#.#  
  #.###.###.###.#.#.###.#.#####.#.#.#                                                             #.#.#.###.#.###.###.#.#.#.#.#.#.#.#  
QP..#...#...........#...#.#.....#.#.#                                                             #...#.....#.........#.............#  
  #.#.#.###.###.#.#.#####.#.#####.###                                                             #.#.#.#.###.###.###.#.#.#.#.###.#.#  
  #...#.....#...#.#.......#.......#.#                                                             #.#.#.#...#.#.#.#...#.#.#.#.#.#.#.#  
  #.#####.###.#.#.#.#.#.###.#.#.#.#.#      O           U     J   J       Z         H       S      ###.#####.#.#.#####.#.#.#####.#.###  
  #.....#.#...#.#.#.#.#.#...#.#.#...#      F           T     Q   B       J         K       K      #.....#.#.#.#.......#.#...#.......#  
  #.#.###.#.#.#.###.#.#.###.###.#.#########.###########.#####.###.#######.#########.#######.###########.#.#####.#.#.#.#####.###.#####  
  #.#...#.#.#.#...#.#.#.#.....#.#...#.......#...#.#...#.#.....#.........#...#...#.....#.#...#...#...........#...#.#.#.....#.#.......#  
  #.#.###.#.#.#.###.#.###.#####.#.#######.###.#.#.#.#.#.###.#######.#######.#.#.#.#####.###.#.###.#####.#.###.#.#####.#########.#.#.#  
  #.#.#.#.#.#.#...#.#...#...#...#...#...#.....#...#.#...#.#...#.#...#...#...#.#.#...#.#.#.......#...#...#...#.#.#.......#.#.....#.#.#  
  #.#.#.###.###.#.#######.#.###.#######.#######.#.#.#####.#.#.#.#.#####.#.###.#.#.###.#.#.#####.#########.###.###.#.###.#.#.###.#.###  
  #.#.#.#...#...#.#.......#...#.#...#.#.....#...#.#...#.....#...#.#...........#.#.......#...#.#.....#.....#.....#.#.#.....#...#.#.#.#  
  #.#.#.#.#.###.###.###.###.#######.#.#.#.#.#.#.#####.#####.#####.###.###.#.###.###.###.###.#.#######.#.#.#######.#.#####.#####.###.#  
  #.#...#.#.#...#.....#.#...#...........#.#...#.#.#.....#.....#.#...#.#...#.#.#...#...#.#.......#...#.#.#...#.....#...#...#.#.......#  
  #.#.###.#.#######.#.#####.#.###.###.###.#######.#.#.###.#####.#.#####.#.###.#.#######.#.###.#.#.#####.#.#####.###.#.###.#.###.###.#  
  #.#...#.#.....#.#.#.#...#.#.#.#...#.#...#.......#.#...#.......#.....#.#...#...#...#.#.#...#.#.#.....#.#.#.#.....#.#.#.....#.#...#.#  
  #.#.#####.#.###.#.#.###.#.###.#.#######.#.#.###.#####.###.###.###.#########.#.#.###.#.#.#####.#.#####.###.#.###.###.###.#.#.#.###.#  
  #.#.#.....#...#.#.#.#.....#.....#.........#.#.....#.#...#.#...#.......#.#...#...#.....#...#.........#.#.....#.#...#.#...#...#...#.#  
  ###.###.###.###.#######.#.#####.###########.#####.#.#.#######.#.#.###.#.#####.#####.###.###.###.###########.#.###.#####.#####.#.#.#  
  #.#.#.#...#...#.....#...#...#...#...............#.#...#.......#.#...#...#.#.....#.#...#...#.#.#.#.#.#.#.#.......#...#.....#...#.#.#  
  #.#.#.#.###.###.#.###.###.#######.#.#.#.#.###########.#####.#.#.#.#####.#.#.#.###.###.#.#####.###.#.#.#.#####.#########.#.#####.###  
  #.....#.#.#...#.#.....#.......#.#.#.#.#.#.#.......#...#.....#.#.#.#.#...#.#.#.#...#...#.....#.#.#.#.#.....#.....#.......#.#...#...#  
  #.#.###.#.#.#######.#.#.###.###.#######.#######.###.#######.###.###.#####.#.#.#.#.###.#.#####.#.#.#.#.###########.#.#.#.###.###.###  
  #.#...#...#.#.....#.#.#.#...#.#.#.#...........#.#.....#.....#...#...#.....#.#...#.#...#...#.#...#.....#.#.....#.#.#.#.#.......#.#.#  
  #.#####.#.#####.#####.#.#.###.#.#.#####.#.#####.#.###.###.#.###.###.###.#.###.#######.#.###.#.###.###.#.###.###.#.#.###.#####.#.#.#  
  #...#...#...#.........#.#.#.........#...#.#.....#.#.....#.#.#.#.....#.#.#.......#.#...#.......#.#.#.#.#.....#...#.#.#.......#.#...#  
  #.###.#.#.#.###.###.###.#######.###.###.#.#####.###.#.#####.#.#.#.###.###.###.###.###.###.#.###.#.#.###.#####.###.#####.#######.#.#  
  #...#.#.#.#.#.#...#...#...#.#.....#...#.#.....#.....#...#.....#.#.#.#.....#.#.#.#.....#...#...............#.....#.....#...#.#...#.#  
  #.###.#.#.###.#.###.#######.#.#.#####.#.#######.#.###.###.###.#.###.###.#.#.###.###.#####.#.#.###.#########.#####.#.#####.#.#######  
  #.#.#.#.#.#.....#...#.#.#.....#.#.......#.#.#.#.#...#.#.#.#.#.#.#.....#.#.....#...#.....#.#.#...#...#...#...#...#.#...#.....#.....#  
  ###.#.###.#.#.###.###.#.#.#.#.###.#####.#.#.#.#.#######.###.#.#.#.#.#.#######.###.###.#######.#########.###.#.#.#.#######.###.#.###  
  #.#...#.#.#.#...#.#.......#.#.#...#...........#.#...#.........#.#.#.#...#.....#.........#.#.#...#.....#.....#.#.#.#.#.#.#.....#...#  
  #.###.#.#.###.#.#.#.#.###.###.#.#######.#.###.#.#.#####.#####.#.###.#.###.#.#.#.###.#####.#.#.#######.#.###.###.###.#.#.###.#.#.#.#  
  #.....#...#...#.#.#.#.#...#...#.#...#...#.#.#.#.......#.#.....#.#...#...#.#.#.#...#.#.#.#.......#.#.......#.#.#.......#.#...#.#.#.#  
  #.#.#########.###.#.#####.###.#####.###.###.#.#######.#####.###.#.###.#####.###.###.#.#.#.#.#.###.#####.###.#.#.#######.#####.###.#  
  #.#.#...........#.#.#.....#.#.#.....#.#.#.....#.#.#.....#...#...#.#.#.#.#.#.#...#.#.#.#...#.#.....#.#.....#.#.#.............#.#...#  
  #######.###.#.###.#.#.#####.###.###.#.#.###.###.#.#.#######.###.#.#.#.#.#.#.###.#.###.#.###.#######.###.#####.#.###################  
  #...#...#...#...#.#.#...#.#...#.#.....#.#.#.....#.....#.......#...#.......#...#.......#.#.#...........#.#.#.#.#.#...........#.#.#.#  
  ###.#.#####.#####.#.###.#.###.#.###.#.###.###.#.#.###.###.#.#.#.#.#.#########.#######.###.#.#.#########.#.#.#.#.#.#####.#.###.#.#.#  
  #.........#.#.....#.#...#.......#...#.........#.#.#.....#.#.#.#.#.#...#.......#...........#.#.........................#.#.........#  
  #########################################.#######.###########.#######.###.#####.#############.#####################################  
                                           L       R           N       L   T     N             Q                                       
                                           P       X           Z       S   V     U             R                                       
"""  # noqa

test_input = """                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               
"""  # noqa


def parse_input(puzzle_input, donut_left=37, donut_right=96, donut_top=37, donut_bottom=88):
    donut = puzzle_input.splitlines()
    donut_map = {}
    portals = {}

    for y, line in enumerate(donut):
        for x, char in enumerate(line):
            donut_map[(x, y)] = 'WALL'
            if char == ' ' or char == '#':
                continue
            elif char == '.':
                donut_map[(x, y)] = 'PATH'
            else:
                # top edge
                if y == 0:
                    portals[(x, 1)] = char
                elif y == 1:
                    portals[(x, 1)] += char
                # bottom edge
                elif y == len(donut) - 2:
                    portals[(x, len(donut) - 2)] = char
                elif y == len(donut) - 1:
                    portals[(x, len(donut) - 2)] += char
                # left edge
                if x == 0:
                    portals[(1, y)] = char
                elif x == 1:
                    portals[(1, y)] += char
                # right edge
                if x == len(line) - 2:
                    portals[(len(line) - 2, y)] = char
                elif x == len(line) - 1:
                    portals[(len(line) - 2, y)] += char
                # inner left edge
                if x == donut_left:
                    portals[(donut_left, y)] = char
                elif x == donut_left + 1:
                    portals[(donut_left, y)] += char
                # inner right edge
                if x == donut_right:
                    portals[(donut_right + 1, y)] = char
                elif x == donut_right + 1:
                    portals[(donut_right + 1, y)] += char
                # inner top edge
                if y == donut_top:
                    portals[(x, donut_top)] = char
                elif y == donut_top + 1:
                    portals[(x, donut_top)] += char
                # inner bottom edge
                if y == donut_bottom:
                    portals[(x, donut_bottom + 1)] = char
                elif y == donut_bottom + 1:
                    portals[(x, donut_bottom + 1)] += char

    portal_map = defaultdict(list)
    for xy, portal in portals.items():
        donut_map[xy] = portal
        portal_map[portal].append(xy)
    return donut_map, portal_map, portals


def traverse_maze(puzzle_input, test=False):
    if test is True:
        donut_map, portal_map, portals = parse_input(puzzle_input, 9, 24, 9, 26)
    else:
        donut_map, portal_map, portals = parse_input(puzzle_input)
    q = deque([portal_map['AA'][0]])
    directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    path = {portal_map['AA'][0]: []}

    while q:
        x, y = q.popleft()
        for direction, dir_xy in directions.items():
            new_xy = (x + dir_xy[0], y + dir_xy[1])
            if new_xy in path:
                continue
            if new_xy in portals:
                portal_label = portals[new_xy]
                if portal_label == 'ZZ':
                    return len(path[(x, y)]) - 1
                portals_xy = portal_map[portal_label]
                for portal in portals_xy:
                    if portal != new_xy:
                        q.append(portal)
                        path[portal] = path[(x, y)]
                continue
            tile = donut_map.get(new_xy)
            path[new_xy] = path[(x, y)] + [new_xy]
            if tile == 'PATH':
                q.append(new_xy)


assert traverse_maze(test_input, test=True) == 58

print(traverse_maze(DAY_20_INPUT))