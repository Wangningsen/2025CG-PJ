import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
w1=cq.Workplane('XY',origin=(0,0,47))
r=w0.workplane(offset=-83/2).moveTo(-22,-70).cylinder(83,30).union(w1.workplane(offset=-26/2).moveTo(47,12).box(10,176,26))