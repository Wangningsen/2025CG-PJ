import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
w1=cq.Workplane('YZ',origin=(75,0,0))
r=w0.workplane(offset=-128/2).moveTo(-40,86).cylinder(128,2).union(w0.sketch().push([(0,-31)]).circle(46).circle(34,mode='s').finalize().extrude(-95)).union(w1.sketch().segment((-27,-88),(-9,-88)).arc((-18,-32),(27,-19)).segment((27,26)).segment((-27,26)).close().assemble().finalize().extrude(25))