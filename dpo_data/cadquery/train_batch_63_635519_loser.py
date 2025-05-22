import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().push([(-50.5,-18.5)]).rect(99,11).reset().face(w0.sketch().segment((-29,8),(-28,4)).segment((20,5)).segment((20,8)).segment((-15,8)).segment((-15,6)).segment((-18,6)).segment((-18,8)).close().assemble()).push([(78,50.5)]).rect(14,3).finalize().extrude(79).union(w1.workplane(offset=-65/2).moveTo(-52.5,55).box(7,90,65))