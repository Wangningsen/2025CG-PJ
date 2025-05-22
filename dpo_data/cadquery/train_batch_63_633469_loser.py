import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('ZX',origin=(0,70,0))
r=w0.sketch().push([(-85,-1)]).circle(15).reset().face(w0.sketch().segment((-77,13),(12,13)).segment((1,3)).segment((65,-70)).segment((100,-39)).segment((34,33)).segment((15,17)).segment((15,29)).segment((-77,29)).close().assemble()).reset().face(w0.sketch().segment((-50,21),(-7,20)).segment((-6,23)).segment((-50,24)).close().assemble(),mode='s').finalize().extrude(14).union(w1.sketch().push([(0,1.5)]).rect(86,15).push([(-17,3)]).circle(3,mode='s').finalize().extrude(-6))