import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
r=w0.sketch().push([(0,58)]).circle(42).push([(5,39.5)]).rect(28,39,mode='s').finalize().extrude(-80).union(w0.sketch().segment((-13,-100),(1,-100)).segment((1,-52)).arc((22,5),(-13,-43)).close().assemble().finalize().extrude(26))