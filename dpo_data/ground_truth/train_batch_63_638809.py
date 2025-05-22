import cadquery as cq
w0=cq.Workplane('YZ',origin=(81,0,0))
r=w0.sketch().segment((-94,-64),(-31,-64)).segment((-31,-100)).segment((87,-100)).segment((87,-64)).segment((94,-64)).segment((94,55)).segment((87,55)).segment((87,100)).segment((-31,100)).segment((-31,55)).segment((-94,55)).close().assemble().finalize().extrude(-163)