import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.sketch().segment((-100,42),(-73,-42)).segment((-36,-30)).arc((20,-35),(63,1)).segment((100,13)).segment((91,42)).close().assemble().finalize().extrude(83)