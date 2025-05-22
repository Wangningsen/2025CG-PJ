import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-42,0))
r=w0.workplane(offset=-58/2).moveTo(15,18).cylinder(58,74).union(w0.sketch().segment((-83,-73),(-83,-62)).segment((-76,-62)).segment((-76,-76)).segment((-81,-76)).arc((-24,-25),(-83,-73)).assemble().push([(-53,-50)]).circle(7,mode='s').finalize().extrude(142))