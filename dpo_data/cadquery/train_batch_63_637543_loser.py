import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,78,0))
r=w0.sketch().arc((-3,-58),(20,0),(-3,58)).close().assemble().finalize().extrude(-156).union(w0.workplane(offset=-119/2).cylinder(119,57)).union(w0.sketch().rect(200,188).rect(20,158,mode='s').finalize().extrude(-102))