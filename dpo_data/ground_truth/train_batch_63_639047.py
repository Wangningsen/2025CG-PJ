import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
r=w0.sketch().push([(-39,-16)]).circle(31).circle(26,mode='s').finalize().extrude(16).union(w0.sketch().arc((-76,-35),(-54,-98),(0,-61)).arc((-42,-62),(-76,-35)).assemble().push([(63,28)]).circle(20).finalize().extrude(45)).union(w0.workplane(offset=69/2).moveTo(-27,47).box(72,106,69))