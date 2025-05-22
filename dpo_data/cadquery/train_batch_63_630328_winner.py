import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,3))
r=w0.workplane(offset=-103/2).moveTo(22,-7).cylinder(103,15).union(w0.sketch().segment((-37,-33),(-6,16)).segment((-31,33)).close().assemble().finalize().extrude(97))