import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.workplane(offset=-74/2).moveTo(49.5,-48).box(39,104,74).union(w1.sketch().arc((-20,25),(72,-77),(4,42)).segment((4,90)).segment((-20,90)).close().assemble().finalize().extrude(106))