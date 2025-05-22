import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().push([(18,-30)]).circle(70).push([(18.5,-30.5)]).rect(43,131,mode='s').finalize().extrude(-100).union(w0.sketch().segment((-88,0),(-11,0)).arc((34,-70),(20,12)).segment((20,100)).segment((-88,100)).close().assemble().push([(-3,-30.5)]).rect(30,3,mode='s').push([(39.5,-30.5)]).rect(29,3,mode='s').finalize().extrude(-3))