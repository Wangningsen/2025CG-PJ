import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().push([(14.5,0)]).rect(23,94).push([(88.5,0)]).rect(23,94).finalize().extrude(-15).union(w0.sketch().segment((-100,-16),(-99,-16)).arc((-99,-13),(-100,-11)).close().assemble().finalize().extrude(112))