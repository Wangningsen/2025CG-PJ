import cadquery as cq
w0=cq.Workplane('YZ',origin=(-50,0,0))
w1=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.sketch().segment((-100,-27),(-63,-27)).arc((-40,-81),(-17,-27)).segment((9,-27)).segment((9,81)).segment((-100,81)).close().assemble().finalize().extrude(-16).union(w0.workplane(offset=45/2).moveTo(-13,-28).cylinder(45,1)).union(w1.sketch().segment((-27,52),(-20,52)).arc((-26,59),(-27,66)).close().assemble().finalize().extrude(112))