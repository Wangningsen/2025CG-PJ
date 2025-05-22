import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().push([(16,-14)]).circle(36).push([(-6,-13)]).circle(2,mode='s').finalize().extrude(-110).union(w0.workplane(offset=83/2).moveTo(-42,60.5).box(22,21,83)).union(w1.workplane(offset=80/2).moveTo(45.5,-19).box(9,104,80))