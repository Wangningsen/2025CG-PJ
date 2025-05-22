import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().segment((-70,66),(-38,-34)).segment((70,0)).segment((38,100)).close().assemble().push([(15,-66)]).circle(34).finalize().extrude(47).union(w1.sketch().segment((-16,-29),(-8,-29)).arc((26,-55),(60,-29)).segment((70,-29)).segment((70,-14)).segment((60,-14)).arc((26,12),(-8,-14)).segment((-16,-14)).close().assemble().finalize().extrude(-30))