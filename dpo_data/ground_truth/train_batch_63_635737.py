import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
r=w0.sketch().circle(51).circle(50,mode='s').finalize().extrude(-83).union(w0.workplane(offset=24/2).cylinder(24,15)).union(w0.workplane(offset=117/2).cylinder(117,2))