import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=-49/2).moveTo(-1,-32).cylinder(49,20).union(w0.sketch().segment((-100,-6),(-99,-8)).arc((-65,-19),(-39,-44)).segment((-18,-63)).segment((39,-3)).segment((-25,60)).close().assemble().push([(19,4)]).circle(3,mode='s').finalize().extrude(91)).union(w1.sketch().segment((50,-12),(83,-12)).segment((83,-5)).arc((100,25),(83,54)).segment((83,63)).segment((50,63)).segment((50,54)).arc((33,25),(50,-5)).close().assemble().finalize().extrude(85))