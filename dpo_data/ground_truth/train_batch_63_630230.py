import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().segment((-100,-3),(-74,-3)).arc((-52,-64),(5,-35)).arc((95,32),(-15,13)).arc((-41,18),(-65,7)).segment((-65,14)).arc((-67,15),(-65,17)).segment((-65,44)).segment((-100,44)).close().assemble().finalize().extrude(100)