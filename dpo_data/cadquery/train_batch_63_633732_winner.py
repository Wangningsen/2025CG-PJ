import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().segment((-70,66),(-38,-34)).segment((70,0)).segment((38,100)).close().assemble().push([(15,-66)]).circle(34).finalize().extrude(47).union(w1.sketch().segment((-17,-30),(-10,-30)).arc((27,-55),(63,-30)).segment((70,-30)).segment((70,-6)).segment((63,-6)).arc((27,20),(-10,-6)).segment((-17,-6)).close().assemble().finalize().extrude(-30))