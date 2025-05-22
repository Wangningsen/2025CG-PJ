import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-49))
w1=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().segment((-28,93),(-26,75)).arc((-33,49),(-20,25)).segment((-18,7)).segment((37,14)).segment((35,32)).arc((43,60),(29,84)).segment((26,100)).close().assemble().push([(34,49)]).circle(1,mode='s').finalize().extrude(3).union(w1.sketch().segment((-92,8),(-91,8)).segment((-91,38)).segment((-58,38)).arc((-92,43),(-92,8)).assemble().finalize().extrude(-65))