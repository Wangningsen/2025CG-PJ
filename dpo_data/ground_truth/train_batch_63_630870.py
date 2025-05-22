import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((11,6),(11,39)).arc((-21,-35),(27,30)).segment((27,6)).close().assemble().finalize().extrude(-200)