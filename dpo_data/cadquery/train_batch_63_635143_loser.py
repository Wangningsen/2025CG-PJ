import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().segment((-100,-39),(13,-39)).segment((13,-52)).segment((23,-52)).segment((23,-78)).segment((83,-78)).segment((83,-31)).segment((79,-31)).segment((100,32)).segment((83,39)).segment((83,75)).segment((23,75)).segment((23,78)).segment((-100,78)).close().assemble().finalize().extrude(-10)