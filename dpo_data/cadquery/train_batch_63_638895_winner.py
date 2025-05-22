import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,85,0))
r=w0.sketch().segment((-100,-35),(-76,-43)).arc((-26,-82),(37,-79)).segment((60,-87)).segment((71,-54)).arc((81,-30),(87,-6)).segment((100,35)).segment((76,43)).arc((26,82),(-37,79)).segment((-60,87)).segment((-71,54)).arc((-81,30),(-87,6)).close().assemble().finalize().extrude(-170)