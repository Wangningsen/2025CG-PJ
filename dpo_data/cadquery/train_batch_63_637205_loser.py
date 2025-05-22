import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
r=w0.sketch().segment((-100,-6),(-83,-20)).segment((-61,6)).segment((-61,-62)).segment((27,-62)).segment((27,62)).segment((-61,62)).segment((-61,18)).segment((-70,27)).close().assemble().finalize().extrude(-35).union(w0.sketch().push([(55,6)]).rect(90,112).push([(81,22)]).circle(8,mode='s').finalize().extrude(99))