import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
r=w0.sketch().push([(-38,60)]).circle(40).push([(-10,-58)]).circle(42).reset().face(w0.sketch().segment((21,-10),(66,-26)).segment((78,6)).segment((33,26)).close().assemble()).push([(50,0)]).rect(44,22,mode='s').finalize().extrude(72)