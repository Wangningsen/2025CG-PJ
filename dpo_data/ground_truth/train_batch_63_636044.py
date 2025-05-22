import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,43,0))
w1=cq.Workplane('YZ',origin=(-67,0,0))
r=w0.sketch().segment((-71,-14),(13,-14)).arc((52,-54),(15,-13)).segment((15,100)).segment((-71,100)).close().assemble().finalize().extrude(-86).union(w1.workplane(offset=-33/2).moveTo(15,43.5).box(14,55,33))