This folder contains 2 python files.
blobfinder.py -- the main code of blob finder
blobsampletest.py --  the example test data provided in the problem

Time:
start  13:50 10/21
finish 14:40 10/21

Detail Design:

Environment:
Python 3.5.0

Solution:
1. Go through the input data, find the occupied node.
2. Check the node's unvisited neighbors to find other occupied one.
3. Update the boundaries.

Data Structure:
1. visited_dict:
    dictionary
    key => node's coordinate,
    value => [occupy_status, visit_status]
2. occupy_status:
    int
    1 => occupied
    0 => not occupied
3. visit_status:
    bool
    True => visited
    False => unvisited (default)
4. edges:
    dictionary
    key => direction
    value => row/column number
5. direction:
    string
    "top" => top boundary
    "Left" => left boundary
    "Bottom" => bottom boundary
    "Right" => right boundary
6. row/column number:
    int
    0-10 (input 10*10 array)
7. node's coordinate
    (int, int)
    0-10 (input 10*10 array)



Input:
10*10 2D-Array with occupy_status

OutPrint:
cell reads
Top
Left
Bottom
Right

Functions:
see code comments







