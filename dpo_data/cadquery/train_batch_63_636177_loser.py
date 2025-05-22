import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-61,-24),(-30,-58)).segment((61,24)).segment((30,58)).segment((18,47)).arc((-3,41),(-8,21)).close().assemble().finalize().extrude(200)