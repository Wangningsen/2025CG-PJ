import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.workplane(offset=80/2).moveTo(6.5,-11.5).box(87,81,80).union(w0.sketch().segment((-54,19),(-39,19)).arc((0,1),(39,19)).segment((54,19)).segment((54,82)).segment((39,82)).arc((0,100),(-39,82)).segment((-54,82)).close().assemble().push([(-23.5,-69.5)]).rect(23,61).finalize().extrude(82)).union(w1.workplane(offset=4/2).moveTo(6.5,-11.5).box(27,39,4))