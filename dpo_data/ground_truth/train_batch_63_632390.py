import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
w1=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().segment((-100,-20),(-99,-20)).arc((-98,-17),(-96,-14)).segment((-100,-14)).close().assemble().finalize().extrude(-79).union(w1.sketch().push([(61,0)]).circle(39).push([(60.5,0)]).rect(15,62,mode='s').finalize().extrude(-101))