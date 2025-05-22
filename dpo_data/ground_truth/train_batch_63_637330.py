import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().segment((33,-11),(36,-19)).segment((58,-11)).segment((56,-3)).close().assemble().finalize().extrude(-75).union(w0.sketch().push([(-79,-34)]).circle(21).reset().face(w0.sketch().segment((91,27),(91,31)).segment((96,31)).segment((96,30)).arc((78,53),(92,27)).close().assemble()).finalize().extrude(-71))