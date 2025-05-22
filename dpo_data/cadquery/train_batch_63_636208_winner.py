import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
r=w0.sketch().segment((-100,-58),(-60,-58)).arc((-51,-63),(-41,-58)).segment((-1,-58)).segment((-1,-46)).segment((-41,-46)).arc((-51,-40),(-60,-46)).segment((-100,-46)).close().assemble().finalize().extrude(-86).union(w0.workplane(offset=-82/2).moveTo(37.5,38).box(125,50,82))