import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().arc((-80,64),(-74,17),(-26,27)).arc((-21,94),(-80,64)).assemble().push([(-56,44)]).circle(4,mode='s').finalize().extrude(-45).union(w0.sketch().arc((-14,-65),(48,-55),(-14,-45)).close().assemble().finalize().extrude(22)).union(w0.workplane(offset=49/2).moveTo(43,-55).cylinder(49,45))