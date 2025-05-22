import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
w1=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().segment((45,-47),(71,-47)).segment((71,-66)).segment((74,-66)).segment((74,-47)).segment((100,-47)).segment((100,-21)).segment((74,-21)).segment((74,9)).segment((71,9)).segment((71,-21)).segment((45,-21)).close().assemble().finalize().extrude(-82).union(w1.sketch().push([(-44.5,12)]).rect(111,108).push([(-44,12)]).circle(19,mode='s').finalize().extrude(22))