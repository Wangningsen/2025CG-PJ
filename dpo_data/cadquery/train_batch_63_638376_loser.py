import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
r=w0.workplane(offset=-100/2).moveTo(67.5,0).box(63,18,100).union(w0.sketch().segment((-99,-24),(-91,-44)).segment((-16,-14)).segment((-24,6)).close().assemble().push([(24,18)]).circle(26).circle(18,mode='s').finalize().extrude(100))