import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-78,0))
r=w0.sketch().arc((-44,-59),(60,-88),(75,18)).arc((-54,86),(-44,-59)).assemble().push([(-9,16)]).circle(83,mode='s').circle(68).finalize().extrude(84).union(w0.workplane(offset=155/2).moveTo(20,-28).cylinder(155,71))