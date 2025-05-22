import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().push([(-9,45)]).circle(55).reset().face(w0.sketch().arc((63,-79),(55,-57),(64,-37)).arc((-11,-57),(63,-79)).assemble()).finalize().extrude(42)