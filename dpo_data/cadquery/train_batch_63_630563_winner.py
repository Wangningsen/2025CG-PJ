import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
r=w0.sketch().segment((17,61),(17,98)).arc((-57,-82),(79,61)).close().assemble().push([(0,-0.5)]).rect(46,115,mode='s').push([(27,-91)]).circle(1,mode='s').finalize().extrude(114)