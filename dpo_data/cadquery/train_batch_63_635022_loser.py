import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.workplane(offset=-69/2).moveTo(27,-30).box(70,14,69).union(w0.sketch().segment((-64,-45),(-39,-44)).segment((-39,-26)).segment((-64,-27)).close().assemble().push([(59,21)]).circle(24).finalize().extrude(33)).union(w1.workplane(offset=-69/2).moveTo(-28,65.5).box(14,69,69))