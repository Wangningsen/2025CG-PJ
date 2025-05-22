import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
r=w0.sketch().segment((-3,-75),(3,-75)).segment((3,-19)).arc((20,0),(3,19)).segment((3,75)).segment((-3,75)).segment((-3,19)).arc((-20,0),(-3,-19)).close().assemble().finalize().extrude(-155).union(w0.workplane(offset=-118/2).cylinder(118,57)).union(w0.sketch().rect(200,188).rect(20,158,mode='s').finalize().extrude(-102))