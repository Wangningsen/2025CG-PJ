import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().push([(18,-30)]).circle(70).push([(18.5,-30.5)]).rect(43,131,mode='s').finalize().extrude(-100).union(w0.sketch().segment((-88,0),(-47,0)).segment((-47,-68)).segment((24,-68)).segment((24,0)).segment((20,0)).segment((20,100)).segment((-88,100)).close().assemble().finalize().extrude(-3))