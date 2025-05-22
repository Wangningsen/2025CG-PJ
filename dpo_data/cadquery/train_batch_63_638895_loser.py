import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-85,0))
r=w0.sketch().segment((-100,-35),(-78,-42)).arc((-27,-82),(38,-79)).segment((60,-87)).segment((73,-47)).arc((82,-27),(88,-5)).segment((100,35)).segment((78,42)).arc((27,82),(-38,79)).segment((-60,87)).segment((-73,47)).arc((-82,27),(-88,5)).close().assemble().finalize().extrude(170)