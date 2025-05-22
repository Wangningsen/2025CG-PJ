import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
r=w0.sketch().segment((56,-86),(56,-17)).arc((-47,4),(56,18)).segment((56,48)).segment((94,48)).arc((-90,27),(63,-82)).arc((59,-74),(56,-65)).segment((56,-64)).close().assemble().finalize().extrude(20)