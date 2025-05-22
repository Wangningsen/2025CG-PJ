import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().segment((-21,-15),(-2,-15)).segment((-2,-8)).arc((12,18),(-2,43)).segment((-2,48)).segment((-14,48)).segment((-14,36)).segment((-21,36)).segment((-21,31)).arc((-28,18),(-21,4)).close().assemble().finalize().extrude(-13).union(w0.sketch().push([(-33,-75)]).circle(25).push([(18.5,77.5)]).rect(79,45).finalize().extrude(39))