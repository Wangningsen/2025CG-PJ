import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
r=w0.workplane(offset=-61/2).moveTo(-48,-65).cylinder(61,35).union(w0.workplane(offset=17/2).moveTo(47,64).cylinder(17,36))