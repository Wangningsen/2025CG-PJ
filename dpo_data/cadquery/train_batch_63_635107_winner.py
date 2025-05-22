import cadquery as cq
w0=cq.Workplane('YZ',origin=(-47,0,0))
r=w0.sketch().arc((-33,-41),(84,-68),(36,42)).arc((-84,72),(-33,-41)).assemble().finalize().extrude(84).union(w0.workplane(offset=94/2).moveTo(-31.5,28).box(83,128,94))