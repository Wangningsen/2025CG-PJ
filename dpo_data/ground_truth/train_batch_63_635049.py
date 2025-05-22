import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.workplane(offset=-19/2).moveTo(-41,-80).cylinder(19,20).union(w0.sketch().segment((-43,27),(-9,-50)).segment((13,-40)).segment((-14,22)).arc((58,80),(-23,36)).close().assemble().finalize().extrude(58)).union(w0.workplane(offset=59/2).moveTo(-15,-7).cylinder(59,51))