import cadquery as cq
w0=cq.Workplane('YZ',origin=(-38,0,0))
w1=cq.Workplane('YZ',origin=(-4,0,0))
r=w0.workplane(offset=37/2).moveTo(64.5,-30.5).box(13,7,37).union(w1.sketch().arc((-49,-1),(-63,-75),(10,-93)).segment((10,-77)).segment((28,-77)).arc((38,-44),(26,-10)).arc((3,99),(-49,-1)).assemble().push([(-5,40)]).circle(45,mode='s').finalize().extrude(42))