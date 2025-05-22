import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().segment((-70,66),(-38,-34)).segment((8,-19)).arc((16,-18),(24,-14)).segment((70,0)).segment((38,100)).segment((-8,85)).arc((-16,83),(-24,80)).close().assemble().push([(15,-66)]).circle(34).finalize().extrude(47).union(w1.sketch().segment((-17,-29),(-10,-29)).arc((26,-55),(62,-29)).segment((70,-29)).segment((70,-6)).segment((62,-6)).arc((26,20),(-10,-6)).segment((-17,-6)).close().assemble().finalize().extrude(-30))