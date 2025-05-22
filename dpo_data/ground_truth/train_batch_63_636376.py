import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.sketch().push([(13.5,43.5)]).rect(63,11).push([(30.5,40.5)]).rect(3,3,mode='s').finalize().extrude(-80).union(w0.sketch().segment((-45,20),(-39,-49)).segment((18,-45)).segment((13,25)).close().assemble().push([(10,-28)]).rect(14,16,mode='s').finalize().extrude(120))