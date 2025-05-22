import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,45,0))
r=w0.sketch().arc((-7,24),(-16,-98),(44,6)).segment((44,100)).segment((-7,100)).close().assemble().finalize().extrude(-89)