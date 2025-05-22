import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().segment((-41,-36),(-21,-36)).arc((-39,0),(-21,36)).segment((-41,36)).close().assemble().finalize().extrude(-126).union(w0.workplane(offset=74/2).moveTo(6,0).box(70,184,74))