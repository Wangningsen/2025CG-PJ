import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,88,0))
r=w0.sketch().push([(-6,80)]).circle(20).reset().face(w0.sketch().segment((15,-84),(21,-84)).segment((21,-77)).arc((11,-100),(18,-75)).segment((15,-75)).close().assemble()).finalize().extrude(-177)