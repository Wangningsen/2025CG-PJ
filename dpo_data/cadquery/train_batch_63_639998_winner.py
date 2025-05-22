import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
r=w0.workplane(offset=-42/2).moveTo(39,-42).box(122,48,42).union(w0.sketch().segment((-100,66),(-96,61)).segment((-89,66)).close().assemble().finalize().extrude(21))