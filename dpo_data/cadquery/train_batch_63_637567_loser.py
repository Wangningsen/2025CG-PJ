import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().arc((12,11),(-32,-94),(37,-6)).arc((51,40),(12,11)).assemble().push([(4,82)]).circle(18).finalize().extrude(-30)