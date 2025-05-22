import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().segment((-22,-16),(-1,-17)).segment((1,-3)).arc((1,35),(-22,2)).close().assemble().finalize().extrude(-13).union(w0.sketch().push([(-33,-75)]).circle(25).push([(18.5,77.5)]).rect(79,45).finalize().extrude(39))