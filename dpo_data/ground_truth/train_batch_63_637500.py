import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().segment((-60,-100),(0,-100)).arc((-6,-59),(28,-35)).segment((28,4)).segment((-60,4)).close().assemble().push([(52.5,51.5)]).rect(15,97).push([(53,95.5)]).rect(4,1,mode='s').finalize().extrude(-8).union(w0.workplane(offset=20/2).moveTo(35,29).cylinder(20,7))