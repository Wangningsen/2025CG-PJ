import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,41))
r=w0.sketch().push([(-84.5,30.5)]).rect(31,75).reset().face(w0.sketch().segment((-87,-4),(-81,-6)).segment((-79,0)).segment((-86,1)).close().assemble(),mode='s').finalize().extrude(-83).union(w0.workplane(offset=-63/2).moveTo(43,-23.5).box(114,89,63))