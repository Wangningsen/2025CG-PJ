import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-45))
r=w0.sketch().push([(-33,-46)]).circle(54).reset().face(w0.sketch().segment((16,44),(78,34)).segment((87,90)).segment((25,100)).close().assemble()).finalize().extrude(90)