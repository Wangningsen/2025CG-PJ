import cadquery as cq
w0=cq.Workplane('YZ',origin=(-62,0,0))
r=w0.workplane(offset=115/2).moveTo(46,44).cylinder(115,54).union(w0.sketch().segment((-100,-83),(-79,-83)).arc((-49,-98),(-16,-83)).segment((0,-83)).segment((0,-17)).arc((-4,-16),(-10,-15)).segment((-10,-4)).segment((-100,-4)).close().assemble().push([(46,44.5)]).rect(48,85).finalize().extrude(123))