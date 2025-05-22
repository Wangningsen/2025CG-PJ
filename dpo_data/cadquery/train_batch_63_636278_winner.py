import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
w1=cq.Workplane('XY',origin=(0,0,36))
r=w0.sketch().segment((-100,-53),(-87,-71)).segment((-31,-32)).segment((-39,-20)).segment((-31,-20)).segment((-31,-13)).segment((-45,-13)).segment((-45,-15)).close().assemble().finalize().extrude(-97).union(w1.sketch().push([(97,16.5)]).rect(6,109).rect(4,5,mode='s').finalize().extrude(25))