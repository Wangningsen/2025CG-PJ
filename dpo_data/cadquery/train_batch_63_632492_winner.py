import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-88,100),(-83,92)).segment((-76,100)).close().assemble().finalize().extrude(-91).union(w1.sketch().push([(56,-68)]).circle(32).push([(49,-41)]).circle(2,mode='s').finalize().extrude(23))