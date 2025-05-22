import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((-96,-100),(96,-100)).segment((96,100)).segment((-96,100)).segment((-96,22)).arc((-92,21),(-96,21)).close().assemble().push([(75,10)]).circle(11,mode='s').finalize().extrude(31)