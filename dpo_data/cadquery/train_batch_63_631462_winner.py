import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
w1=cq.Workplane('YZ',origin=(-46,0,0))
r=w0.sketch().segment((-100,-56),(-87,-74)).segment((-75,-65)).segment((-87,-48)).close().assemble().finalize().extrude(-11).union(w1.sketch().segment((-33,-59),(-25,-59)).segment((-25,-60)).segment((72,-60)).segment((72,-59)).segment((74,-59)).segment((74,59)).segment((72,59)).segment((72,60)).segment((-25,60)).segment((-25,59)).segment((-33,59)).close().assemble().finalize().extrude(146))