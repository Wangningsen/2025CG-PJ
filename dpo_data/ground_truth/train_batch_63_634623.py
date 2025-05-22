import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().segment((-91,-100),(-60,-100)).arc((-62,-38),(-32,18)).segment((-38,21)).segment((-36,25)).segment((-29,20)).arc((27,52),(91,51)).segment((91,100)).segment((-91,100)).close().assemble().finalize().extrude(49)