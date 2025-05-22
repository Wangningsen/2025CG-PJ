import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().push([(-48,-38)]).circle(41).reset().face(w0.sketch().segment((-2,-12),(2,-20)).segment((65,20)).segment((89,20)).segment((89,79)).segment((18,79)).segment((18,20)).segment((39,20)).close().assemble()).finalize().extrude(-79).union(w0.workplane(offset=121/2).moveTo(41,13).cylinder(121,48))