import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().push([(-9,45)]).circle(55).reset().face(w0.sketch().arc((63,-40),(-11,-61),(64,-79)).arc((55,-60),(63,-40)).assemble()).finalize().extrude(-42)