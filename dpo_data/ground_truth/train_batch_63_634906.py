import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
r=w0.workplane(offset=-16/2).moveTo(42,28).cylinder(16,58).union(w0.sketch().segment((-100,-54),(-24,-86)).segment((-18,-71)).segment((-94,-40)).close().assemble().finalize().extrude(1))