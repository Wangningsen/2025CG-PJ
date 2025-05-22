import cadquery as cq
w0=cq.Workplane('YZ',origin=(-60,0,0))
r=w0.sketch().segment((37,96),(41,96)).segment((41,98)).segment((42,98)).segment((42,100)).segment((37,100)).close().assemble().finalize().extrude(37).union(w0.sketch().push([(-79,-92)]).circle(8).push([(19,-20)]).circle(68).circle(36,mode='s').finalize().extrude(121))