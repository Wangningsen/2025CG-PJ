import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.workplane(offset=-200/2).moveTo(34,-42).cylinder(200,40).union(w0.sketch().segment((-44,-23),(-37,-23)).arc((4,77),(-44,-20)).close().assemble().push([(-18,27.5)]).rect(30,31,mode='s').finalize().extrude(-102))