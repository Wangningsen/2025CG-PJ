import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().arc((-66,-19),(-67,-45),(-43,-50)).arc((-33,-45),(-24,-39)).arc((83,-30),(-10,24)).arc((-54,20),(-66,-19)).assemble().push([(28.5,-16.5)]).rect(35,33,mode='s').finalize().extrude(-97).union(w0.workplane(offset=103/2).moveTo(-81,24).box(8,98,103))