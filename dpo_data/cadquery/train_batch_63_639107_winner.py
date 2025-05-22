import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().push([(-16,32)]).circle(47).push([(-45,-2)]).circle(1,mode='s').finalize().extrude(-87).union(w1.workplane(offset=75/2).moveTo(59.5,-74).box(5,10,75))