import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-84))
w1=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().segment((-65,-100),(-52,-100)).segment((-52,-22)).arc((-29,-28),(-5,-25)).arc((73,56),(-39,74)).arc((-74,36),(-65,-11)).close().assemble().finalize().extrude(75).union(w1.workplane(offset=-79/2).moveTo(19,-58.5).box(130,35,79))