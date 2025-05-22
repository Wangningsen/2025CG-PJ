import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-87,0))
r=w0.sketch().segment((-100,-48),(-55,-48)).segment((-55,-82)).segment((70,-82)).segment((70,-48)).segment((100,-48)).segment((100,-21)).arc((75,-31),(50,-35)).segment((50,-52)).segment((-35,-52)).segment((-35,-20)).segment((-6,-20)).arc((-45,24),(-53,82)).segment((-100,82)).close().assemble().finalize().extrude(174)