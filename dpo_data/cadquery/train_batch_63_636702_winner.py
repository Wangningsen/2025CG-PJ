import cadquery as cq
w0=cq.Workplane('YZ',origin=(72,0,0))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().push([(-44.5,12)]).rect(111,108).reset().face(w0.sketch().segment((-66,11),(-31,-3)).segment((-23,17)).segment((-58,26)).close().assemble(),mode='s').finalize().extrude(-22).union(w1.sketch().segment((45,-47),(71,-47)).segment((71,-66)).segment((74,-66)).segment((74,-47)).segment((100,-47)).segment((100,-21)).segment((74,-21)).segment((74,9)).segment((71,9)).segment((71,-21)).segment((45,-21)).close().assemble().finalize().extrude(-82))