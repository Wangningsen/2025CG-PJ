import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.workplane(offset=-72/2).moveTo(63,2).cylinder(72,37).union(w0.sketch().segment((-100,-55),(-60,-79)).segment((-33,-30)).segment((-73,-4)).close().assemble().push([(7,71)]).circle(9).finalize().extrude(19)).union(w1.sketch().push([(-14,8)]).circle(55).push([(-14,8.5)]).rect(88,39,mode='s').finalize().extrude(87))