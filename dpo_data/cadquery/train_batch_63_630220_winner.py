import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-19,-100),(-9,-100)).arc((4,-80),(13,-100)).segment((69,-100)).segment((69,-44)).segment((-19,-44)).close().assemble().finalize().extrude(-41).union(w0.sketch().arc((-62,74),(5,11),(-29,96)).arc((-53,96),(-62,74)).assemble().finalize().extrude(53))