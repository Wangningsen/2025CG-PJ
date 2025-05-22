import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
r=w0.sketch().segment((-87,-64),(-10,-86)).arc((-1,-67),(-3,-88)).segment((40,-100)).segment((87,64)).segment((-40,100)).close().assemble().circle(62,mode='s').finalize().extrude(-88)