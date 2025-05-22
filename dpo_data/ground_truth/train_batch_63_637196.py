import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
w1=cq.Workplane('XY',origin=(0,0,-56))
r=w0.sketch().push([(-63,0)]).circle(34).push([(-91,1)]).circle(5,mode='s').reset().face(w0.sketch().segment((-77,-5),(-65,-5)).segment((-65,2)).arc((-60,11),(-65,19)).segment((-65,27)).segment((-77,27)).segment((-77,19)).arc((-82,11),(-77,2)).close().assemble(),mode='s').finalize().extrude(-95).union(w1.sketch().circle(100).rect(184,50,mode='s').finalize().extrude(153))