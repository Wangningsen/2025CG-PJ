import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,47))
r=w0.sketch().arc((-64,-45),(2,-98),(37,-25)).segment((74,-25)).segment((74,100)).segment((-58,100)).segment((-58,-25)).segment((1,-25)).arc((-15,-44),(-40,-51)).arc((-51,-49),(-61,-45)).close().assemble().finalize().extrude(-94).union(w0.workplane(offset=-32/2).moveTo(-11,-48).box(126,98,32))