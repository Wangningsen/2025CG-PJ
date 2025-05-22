import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.workplane(offset=-57/2).moveTo(71,8).cylinder(57,29).union(w0.sketch().segment((-100,15),(-55,-11)).arc((-40,-54),(2,-58)).arc((93,-49),(19,1)).arc((-1,15),(-26,16)).segment((-7,57)).segment((-57,88)).close().assemble().push([(37.5,73)]).rect(33,6).finalize().extrude(64))