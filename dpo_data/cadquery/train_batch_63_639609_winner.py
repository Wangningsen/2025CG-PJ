import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().push([(-9,45)]).circle(55).reset().face(w0.sketch().arc((63,-39),(-11,-60),(64,-80)).arc((55,-59),(63,-39)).assemble()).finalize().extrude(42)