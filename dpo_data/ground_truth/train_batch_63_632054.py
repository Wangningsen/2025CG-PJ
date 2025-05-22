import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().push([(-80,40)]).circle(1).push([(-48,69)]).circle(31).reset().face(w0.sketch().segment((7,-85),(42,-100)).segment((81,-7)).segment((45,8)).close().assemble()).finalize().extrude(96)