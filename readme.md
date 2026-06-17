install the PlaneSections library using the python pip coommand 
# pip install planesections
# import planesections as ps

Creating Beam Model
Define node locations, and support conditions
# L = 25 # beam length in meters

Create Support Conditions
Define beam with support conditions or fixities

# key for support conditions or fixities  = {'free':[0,0,0], 'roller': [0,1,0], 'pinned':[1,1,0], 'fixed':[1,1,1]}
