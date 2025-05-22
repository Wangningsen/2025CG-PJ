import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().arc((-32,1),(-79,-83),(10,-45)).arc((11,-45),(13,-46)).arc((15,-38),(17,-32)).arc((63,88),(-32,1)).assemble().finalize().extrude(-63).union(w0.sketch().segment((19,-77),(23,-77)).arc((21,-75),(19,-72)).close().assemble().finalize().extrude(-49))