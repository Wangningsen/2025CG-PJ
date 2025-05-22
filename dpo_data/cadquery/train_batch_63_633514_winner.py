import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,46,0))
w1=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((39,-7),(42,-7)).segment((42,-2)).arc((99,35),(66,92)).segment((67,99)).segment((62,100)).segment((62,94)).arc((4,58),(39,-2)).close().assemble().finalize().extrude(-92).union(w0.workplane(offset=-46/2).moveTo(-48.5,18).box(103,68,46)).union(w1.workplane(offset=-111/2).moveTo(8.5,-46).box(51,52,111))