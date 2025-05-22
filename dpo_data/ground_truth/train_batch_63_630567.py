import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().push([(-43,0)]).circle(57).reset().face(w0.sketch().segment((54,16),(75,-4)).segment((100,22)).segment((72,48)).segment((72,19)).segment((54,19)).close().assemble()).finalize().extrude(-111)