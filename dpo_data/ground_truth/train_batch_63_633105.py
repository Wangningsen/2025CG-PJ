import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.sketch().arc((79,23),(10,-62),(88,14)).segment((88,23)).close().assemble().finalize().extrude(-130).union(w0.sketch().segment((-100,53),(-63,27)).segment((-74,11)).arc((-58,17),(-48,31)).segment((-65,36)).segment((-54,75)).segment((-71,67)).close().assemble().finalize().extrude(-53))