import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().push([(18,-30)]).circle(70).rect(44,132,mode='s').finalize().extrude(-100).union(w0.sketch().segment((-88,0),(-21,0)).segment((-21,-77)).segment((16,-77)).segment((16,0)).segment((20,0)).segment((20,100)).segment((-88,100)).close().assemble().finalize().extrude(-3))