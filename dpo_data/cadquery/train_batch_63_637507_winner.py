import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
w1=cq.Workplane('YZ',origin=(-92,0,0))
r=w0.workplane(offset=-101/2).moveTo(87.5,-45).box(15,110,101).union(w0.sketch().segment((0,-85),(81,-85)).segment((81,-58)).arc((96,-16),(81,22)).segment((81,52)).segment((0,52)).segment((0,22)).arc((-15,-16),(0,-54)).close().assemble().finalize().extrude(-71)).union(w1.workplane(offset=-4/2).moveTo(41,41).box(118,64,4))