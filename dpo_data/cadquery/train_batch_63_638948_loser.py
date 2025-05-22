import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,1))
r=w0.workplane(offset=-98/2).moveTo(-74,-71).cylinder(98,26).union(w0.sketch().push([(-74,-71)]).circle(12).circle(9,mode='s').push([(13,79)]).rect(174,36).push([(-70,76)]).circle(3,mode='s').finalize().extrude(96))