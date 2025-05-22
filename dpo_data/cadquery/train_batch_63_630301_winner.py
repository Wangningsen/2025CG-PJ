import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().push([(-1,0)]).rect(134,158).push([(-46,49)]).circle(21,mode='s').finalize().extrude(159).union(w0.sketch().segment((28,-50),(37,-64)).segment((68,-31)).segment((34,-5)).arc((33,-5),(33,-6)).arc((34,-11),(30,-11)).arc((28,-30),(31,-48)).close().assemble().finalize().extrude(200))