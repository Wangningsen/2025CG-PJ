import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
r=w0.workplane(offset=-47/2).moveTo(-22,-97.5).box(40,5,47).union(w0.sketch().arc((-69,79),(-55,64),(-62,44)).arc((-44,35),(-25,38)).arc((64,14),(-7,72)).arc((-36,100),(-69,79)).assemble().push([(22,35)]).circle(6,mode='s').finalize().extrude(2))