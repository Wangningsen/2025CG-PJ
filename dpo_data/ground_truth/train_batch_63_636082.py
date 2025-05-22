import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().segment((-90,4),(-84,4)).segment((-84,-10)).segment((-8,-10)).segment((-8,4)).segment((-2,4)).segment((-2,78)).segment((-8,78)).segment((-8,92)).segment((-84,92)).segment((-84,78)).segment((-90,78)).close().assemble().push([(41,-51)]).circle(49).finalize().extrude(-50).union(w1.sketch().segment((-15,-70),(56,-70)).segment((56,-49)).segment((44,-49)).segment((44,-22)).segment((-15,-22)).close().assemble().finalize().extrude(82))