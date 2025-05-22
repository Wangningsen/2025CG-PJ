import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,67))
r=w0.workplane(offset=-135/2).moveTo(48,0).cylinder(135,52).union(w0.workplane(offset=-22/2).moveTo(-81,1).cylinder(22,19))