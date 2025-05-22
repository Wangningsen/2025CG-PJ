import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().segment((-51,33),(11,33)).segment((11,16)).segment((25,16)).segment((25,33)).segment((83,33)).segment((83,62)).segment((25,62)).segment((25,86)).segment((11,86)).segment((11,62)).segment((-51,62)).close().assemble().finalize().extrude(-14).union(w0.workplane(offset=100/2).moveTo(65,95).cylinder(100,5)).union(w1.sketch().push([(-15.5,-36)]).rect(135,128).push([(16,23)]).circle(3,mode='s').finalize().extrude(-132))