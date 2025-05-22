import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().arc((-20,24),(71,-77),(4,42)).segment((4,90)).segment((-20,90)).close().assemble().finalize().extrude(-106).union(w1.workplane(offset=-104/2).moveTo(-5.5,49.5).box(75,39,104))