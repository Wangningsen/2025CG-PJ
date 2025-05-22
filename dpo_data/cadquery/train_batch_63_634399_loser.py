import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().push([(-42,-38)]).circle(58).reset().face(w0.sketch().segment((44,13),(55,-62)).segment((92,-57)).segment((82,16)).segment((66,13)).arc((58,96),(49,13)).close().assemble()).reset().face(w0.sketch().segment((41,81),(71,26)).segment((73,27)).segment((43,82)).close().assemble(),mode='s').finalize().extrude(64)