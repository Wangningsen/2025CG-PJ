import cadquery as cq
w0=cq.Workplane('YZ',origin=(91,0,0))
r=w0.workplane(offset=-182/2).moveTo(-1,-58).cylinder(182,36).union(w0.sketch().arc((24,39),(43,74),(39,100)).close().assemble().finalize().extrude(-130)).union(w0.workplane(offset=-46/2).moveTo(-1,-58).cylinder(46,42))