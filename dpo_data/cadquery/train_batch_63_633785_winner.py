import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,95))
r=w0.workplane(offset=-195/2).box(108,174,195).union(w0.sketch().segment((-48,-28),(-14,-28)).arc((-16,0),(-10,28)).segment((-48,28)).close().assemble().finalize().extrude(5))