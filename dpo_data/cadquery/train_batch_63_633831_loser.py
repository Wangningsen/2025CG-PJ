import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,49))
r=w0.workplane(offset=-98/2).moveTo(-49,2).box(86,74,98).union(w0.sketch().arc((-19,42),(-99,-9),(-7,-24)).arc((-4,-24),(-1,-25)).segment((-1,-49)).segment((16,-49)).arc((98,14),(-3,29)).arc((-11,34),(-19,42)).assemble().finalize().extrude(-79))