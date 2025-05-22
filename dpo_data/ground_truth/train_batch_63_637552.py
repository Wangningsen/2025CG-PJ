import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().segment((56,-82),(56,-17)).arc((-47,0),(56,17)).segment((56,48)).segment((94,48)).arc((-91,23),(64,-82)).close().assemble().finalize().extrude(-20)