import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
r=w0.sketch().push([(-54,-74)]).circle(26).reset().face(w0.sketch().segment((8,27),(55,11)).segment((80,84)).segment((34,100)).close().assemble()).finalize().extrude(62)