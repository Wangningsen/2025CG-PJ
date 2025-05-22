import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,3))
r=w0.workplane(offset=-89/2).moveTo(-31,-16).cylinder(89,69).union(w0.workplane(offset=82/2).moveTo(13,0).cylinder(82,87))