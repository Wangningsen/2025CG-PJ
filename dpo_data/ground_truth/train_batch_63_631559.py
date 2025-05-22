import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
r=w0.sketch().segment((43,80),(65,54)).segment((88,75)).segment((65,100)).close().assemble().finalize().extrude(18).union(w0.workplane(offset=26/2).moveTo(-37,-40.5).box(102,119,26))