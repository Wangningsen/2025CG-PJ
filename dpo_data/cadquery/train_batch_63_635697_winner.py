import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
w1=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().arc((-85,-10),(-65,-96),(11,-45)).segment((15,-45)).segment((15,2)).arc((96,61),(-4,71)).arc((-78,74),(-85,-3)).close().assemble().finalize().extrude(50).union(w1.sketch().segment((-15,-73),(19,-73)).segment((19,-66)).segment((15,-66)).segment((15,-7)).segment((19,-7)).segment((19,10)).segment((-15,10)).close().assemble().push([(79,-29)]).rect(20,88).finalize().extrude(45))