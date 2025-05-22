import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().arc((-38,-52),(-16,14),(46,45)).arc((-49,42),(-38,-52)).assemble().finalize().extrude(-200).union(w0.workplane(offset=-35/2).cylinder(35,86))