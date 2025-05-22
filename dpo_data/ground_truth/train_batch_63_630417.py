import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
r=w0.sketch().push([(-87,71)]).circle(13).reset().face(w0.sketch().arc((-88,-50),(-30,-81),(-5,-20)).arc((-15,8),(-43,18)).arc((-81,34),(-75,-6)).arc((-83,-16),(-88,-27)).arc((-98,-38),(-88,-50)).assemble()).push([(-42,-61)]).circle(6,mode='s').push([(58,-8.5)]).rect(84,43).finalize().extrude(11)