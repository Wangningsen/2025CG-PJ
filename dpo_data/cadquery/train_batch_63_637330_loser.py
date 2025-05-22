import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().segment((33,-11),(36,-19)).segment((58,-11)).segment((56,-3)).close().assemble().finalize().extrude(-76).union(w0.sketch().push([(-79,-34)]).circle(21).push([(85,40)]).circle(15).push([(93,30)]).circle(2,mode='s').finalize().extrude(-72))