import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().arc((-86,66),(-19,35),(-54,99)).arc((-82,94),(-86,66)).assemble().finalize().extrude(-93).union(w1.workplane(offset=91/2).moveTo(15,-27).cylinder(91,73))