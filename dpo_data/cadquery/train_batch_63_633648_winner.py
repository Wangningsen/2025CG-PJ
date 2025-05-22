import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.workplane(offset=-65/2).moveTo(-8.5,35).box(35,130,65).union(w0.sketch().segment((-41,24),(23,-10)).segment((41,25)).segment((-23,59)).close().assemble().push([(-7,-95)]).circle(5).finalize().extrude(78))