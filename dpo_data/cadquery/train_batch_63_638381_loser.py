import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
w1=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().segment((-42,87),(-41,84)).segment((-38,85)).segment((-39,88)).close().assemble().finalize().extrude(-175).union(w0.sketch().segment((-27,-88),(-8,-88)).arc((-18,-76),(-22,-61)).segment((-25,-61)).segment((-25,-52)).segment((-22,-52)).arc((-1,-22),(27,-19)).segment((27,26)).segment((-27,26)).close().assemble().finalize().extrude(25)).union(w1.sketch().push([(0,-31)]).circle(46).circle(34,mode='s').finalize().extrude(-95))