import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-19,-100),(-9,-100)).arc((2,-80),(13,-100)).segment((69,-100)).segment((69,-44)).segment((-19,-44)).close().assemble().finalize().extrude(-41).union(w0.sketch().arc((-63,73),(6,11),(-22,97)).arc((-51,97),(-63,73)).assemble().finalize().extrude(53))