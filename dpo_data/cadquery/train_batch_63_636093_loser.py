import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
r=w0.sketch().arc((-20,-21),(-37,-73),(-9,-25)).segment((24,-25)).segment((24,-2)).segment((-20,-2)).close().assemble().push([(1.5,70)]).rect(75,60).push([(49,-96)]).circle(4).finalize().extrude(20).union(w0.sketch().push([(2,-13)]).circle(12).push([(8.5,-13.5)]).rect(3,11,mode='s').finalize().extrude(78))