import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('YZ',origin=(-66,0,0))
r=w0.sketch().segment((-29,-34),(-25,-34)).segment((-25,-10)).segment((-29,-10)).segment((-29,-16)).segment((-27,-16)).segment((-27,-18)).segment((-29,-18)).close().assemble().finalize().extrude(4).union(w0.sketch().segment((-27,52),(-20,52)).arc((-24,59),(-27,66)).close().assemble().finalize().extrude(114)).union(w1.sketch().segment((-100,-27),(-63,-27)).arc((-40,-81),(-18,-27)).segment((9,-27)).segment((9,81)).segment((-100,81)).close().assemble().finalize().extrude(16))