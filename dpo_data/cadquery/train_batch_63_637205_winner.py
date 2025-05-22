import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
r=w0.sketch().segment((-100,-11),(-86,-19)).segment((-61,25)).segment((-61,-62)).segment((27,-62)).segment((27,62)).segment((-61,62)).segment((-61,30)).segment((-71,37)).close().assemble().finalize().extrude(-35).union(w0.sketch().push([(55,6)]).rect(90,112).push([(80,22)]).circle(8,mode='s').finalize().extrude(99))