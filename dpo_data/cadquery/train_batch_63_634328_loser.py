import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,44))
w1=cq.Workplane('XY',origin=(0,0,43))
r=w0.sketch().segment((-76,93),(-67,41)).segment((-24,48)).segment((-33,100)).close().assemble().finalize().extrude(33).union(w1.workplane(offset=-120/2).moveTo(71.5,-54).box(9,92,120))