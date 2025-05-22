import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().arc((15,10),(-40,-89),(37,-6)).arc((53,39),(15,10)).assemble().push([(4,82)]).circle(18).finalize().extrude(-30)