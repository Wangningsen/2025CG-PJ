import cadquery as cq
w0=cq.Workplane('YZ',origin=(-47,0,0))
r=w0.sketch().arc((-28,-43),(85,-67),(37,42)).arc((-85,71),(-28,-43)).assemble().finalize().extrude(84).union(w0.workplane(offset=94/2).moveTo(-31.5,28).box(83,128,94))