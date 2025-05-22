import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((11,6),(27,6)).segment((27,30)).arc((-19,-36),(12,39)).segment((11,39)).close().assemble().finalize().extrude(-200)