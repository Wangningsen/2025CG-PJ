import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().arc((-6,-51),(6,0),(-6,51)).close().assemble().finalize().extrude(200)