import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.workplane(offset=16/2).moveTo(-40.5,-19.5).box(57,51,16).union(w0.sketch().arc((-76,-35),(-56,-97),(0,-61)).arc((-40,-63),(-76,-35)).assemble().push([(63,28)]).circle(20).finalize().extrude(45)).union(w0.workplane(offset=69/2).moveTo(-27,47).box(72,106,69))