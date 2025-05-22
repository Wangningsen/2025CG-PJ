import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-56,0))
r=w0.sketch().arc((-81,58),(87,-50),(-78,62)).segment((-81,62)).close().assemble().finalize().extrude(113)