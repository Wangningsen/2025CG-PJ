import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().push([(-97,89)]).circle(3).reset().face(w0.sketch().segment((-64,-34),(-7,-91)).segment((100,12)).segment((43,70)).close().assemble()).finalize().extrude(-51)