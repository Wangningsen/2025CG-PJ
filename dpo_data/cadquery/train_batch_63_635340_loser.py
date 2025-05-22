import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.sketch().segment((-87,-64),(40,-100)).segment((87,64)).segment((-40,100)).close().assemble().circle(62,mode='s').reset().face(w0.sketch().segment((-13,-75),(13,-85)).segment((19,-66)).segment((-7,-66)).close().assemble(),mode='s').finalize().extrude(88)