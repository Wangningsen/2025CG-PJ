import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.workplane(offset=80/2).moveTo(6.5,-7.5).box(87,89,80).union(w0.sketch().segment((-54,19),(-39,19)).arc((0,1),(39,19)).segment((54,19)).segment((54,82)).segment((39,82)).arc((0,100),(-39,82)).segment((-54,82)).close().assemble().push([(-23.5,-64.5)]).rect(23,71).finalize().extrude(83))