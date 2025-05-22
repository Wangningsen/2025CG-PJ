import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('ZX',origin=(0,-31,0))
r=w0.sketch().segment((-57,-91),(57,-91)).segment((57,40)).segment((50,40)).arc((28,46),(5,40)).segment((-57,40)).close().assemble().finalize().extrude(14).union(w0.sketch().push([(0,28)]).rect(142,22).circle(9,mode='s').finalize().extrude(66)).union(w1.workplane(offset=-69/2).moveTo(0,28).cylinder(69,63))