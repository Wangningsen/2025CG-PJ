import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
w1=cq.Workplane('ZX',origin=(0,61,0))
r=w0.sketch().circle(100).push([(22,-11)]).circle(71,mode='s').finalize().extrude(48).union(w1.workplane(offset=30/2).moveTo(0,-4.5).box(112,119,30))