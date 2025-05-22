import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().circle(32).circle(26,mode='s').finalize().extrude(3).union(w1.sketch().segment((-96,-100),(96,-100)).segment((96,100)).segment((-96,100)).segment((-96,21)).arc((-92,20),(-96,19)).close().assemble().push([(77,10)]).circle(10,mode='s').finalize().extrude(-31))