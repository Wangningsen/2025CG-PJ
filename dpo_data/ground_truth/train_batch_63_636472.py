import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('ZX',origin=(0,59,0))
r=w0.workplane(offset=-72/2).moveTo(63,2).cylinder(72,37).union(w0.sketch().segment((-100,-59),(-58,-80)).segment((-30,-23)).segment((-72,-2)).close().assemble().push([(9,71)]).circle(9).push([(9.5,70.5)]).rect(1,7,mode='s').finalize().extrude(19)).union(w1.sketch().push([(-14,8)]).circle(55).push([(-14,8.5)]).rect(88,39,mode='s').finalize().extrude(-87))