import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-42,34),(-24,34)).segment((-24,70)).segment((-22,70)).segment((-22,71)).segment((22,71)).segment((22,70)).segment((42,70)).segment((42,89)).segment((9,89)).segment((9,100)).segment((-9,100)).segment((-9,89)).segment((-42,89)).close().assemble().push([(15,-17)]).circle(11).finalize().extrude(22).union(w1.workplane(offset=-5/2).moveTo(-9,-70).cylinder(5,30))