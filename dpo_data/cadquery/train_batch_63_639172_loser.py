import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-76,0))
w1=cq.Workplane('XY',origin=(0,0,-47))
r=w0.workplane(offset=176/2).moveTo(34,47).box(26,10,176).union(w1.workplane(offset=83/2).moveTo(-22,-70).cylinder(83,30))