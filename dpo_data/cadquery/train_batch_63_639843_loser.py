import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.workplane(offset=-59/2).moveTo(28,0).cylinder(59,72).union(w0.sketch().segment((-100,-23),(44,-65)).segment((70,23)).segment((-73,66)).close().assemble().finalize().extrude(32))