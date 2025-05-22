import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().arc((-19,0),(-12,-19),(-1,-2)).arc((-6,37),(-19,0)).assemble().finalize().extrude(-13).union(w0.sketch().push([(-33,-75)]).circle(25).push([(18.5,77.5)]).rect(79,45).finalize().extrude(39))