import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,2))
w1=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().segment((-49,47),(-49,83)).segment((5,83)).arc((-42,94),(-49,47)).assemble().reset().face(w0.sketch().arc((-15,-17),(12,-25),(38,-17)).close().assemble()).reset().face(w0.sketch().arc((49,-8),(62,26),(49,60)).close().assemble()).push([(55,71)]).circle(4).finalize().extrude(-57).union(w1.sketch().arc((-19,-48),(-1,-36),(-8,-57)).arc((39,14),(-19,-48)).assemble().push([(13,-20)]).circle(18,mode='s').finalize().extrude(-101))