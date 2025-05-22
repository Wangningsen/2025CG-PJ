import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-58))
r=w0.sketch().segment((62,-84),(62,-62)).segment((92,-62)).arc((9,9),(69,-84)).close().assemble().finalize().extrude(92).union(w0.workplane(offset=117/2).moveTo(-84,73).cylinder(117,16))