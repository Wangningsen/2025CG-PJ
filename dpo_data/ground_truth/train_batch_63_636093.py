import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().arc((-20,-21),(-36,-74),(-10,-25)).segment((24,-25)).segment((24,-10)).segment((19,-2)).segment((-20,-2)).close().assemble().push([(1.5,70)]).rect(75,60).push([(49,-96)]).circle(4).finalize().extrude(19).union(w0.sketch().push([(2,-13)]).circle(12).push([(8.5,-13.5)]).rect(3,9,mode='s').finalize().extrude(77))