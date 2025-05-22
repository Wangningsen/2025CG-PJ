import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().segment((-100,-23),(-33,-23)).segment((-33,-30)).segment((-19,-30)).segment((25,-66)).segment((100,26)).segment((50,66)).segment((18,26)).segment((18,-5)).segment((-100,-5)).close().assemble().finalize().extrude(-71)