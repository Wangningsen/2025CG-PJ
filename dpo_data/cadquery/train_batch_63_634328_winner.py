import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,44))
w1=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().segment((-76,93),(-67,41)).segment((-24,48)).segment((-33,100)).close().assemble().finalize().extrude(33).union(w1.workplane(offset=-92/2).moveTo(-16.5,71.5).box(119,9,92))