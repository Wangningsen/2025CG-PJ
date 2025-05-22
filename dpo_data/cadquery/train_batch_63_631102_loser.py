import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
r=w0.sketch().push([(-69,-84)]).circle(16).reset().face(w0.sketch().segment((-45,54),(48,-20)).segment((85,25)).segment((-7,100)).close().assemble()).finalize().extrude(-73)