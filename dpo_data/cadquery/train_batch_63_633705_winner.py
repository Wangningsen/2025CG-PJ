import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.workplane(offset=81/2).moveTo(6.5,-10.5).box(87,83,81).union(w0.sketch().segment((-54,19),(-39,19)).arc((0,-1),(39,19)).segment((54,19)).segment((54,82)).segment((39,82)).arc((0,100),(-39,82)).segment((-54,82)).close().assemble().push([(-23.5,-63.5)]).rect(23,73).finalize().extrude(83))