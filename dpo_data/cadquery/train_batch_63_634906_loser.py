import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,8))
r=w0.workplane(offset=-17/2).moveTo(42,28).cylinder(17,58).union(w0.sketch().segment((-100,-54),(-25,-86)).segment((-19,-73)).segment((-95,-42)).close().assemble().finalize().extrude(1))