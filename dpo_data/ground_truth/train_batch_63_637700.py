import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('YZ',origin=(-50,0,0))
r=w0.sketch().arc((-29,-35),(-24,-20),(-29,-4)).close().assemble().finalize().extrude(2).union(w0.sketch().segment((-27,52),(-20,52)).arc((-24,59),(-27,66)).close().assemble().finalize().extrude(114)).union(w1.sketch().segment((-100,-27),(-62,-27)).arc((-41,-81),(-19,-27)).segment((9,-27)).segment((9,81)).segment((-100,81)).close().assemble().finalize().extrude(-16))