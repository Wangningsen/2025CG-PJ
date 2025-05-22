import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-49))
r=w0.sketch().push([(14.5,0)]).rect(23,94).push([(88.5,0)]).rect(23,94).finalize().extrude(-14).union(w0.sketch().segment((-100,-16),(-99,-16)).segment((-100,-11)).close().assemble().finalize().extrude(112))