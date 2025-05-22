import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=-49/2).moveTo(-1,-32).cylinder(49,20).union(w0.sketch().arc((-100,-6),(-89,-7),(-79,-5)).segment((-18,-63)).segment((40,-2)).segment((-25,60)).segment((-81,2)).close().assemble().push([(20,4)]).circle(3,mode='s').finalize().extrude(91)).union(w1.sketch().segment((50,-12),(83,-12)).segment((83,-4)).arc((100,25),(83,55)).segment((83,63)).segment((50,63)).segment((50,55)).arc((33,25),(50,-4)).close().assemble().finalize().extrude(85))