import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().arc((-84,23),(-63,58),(-46,15)).arc((-48,99),(-84,23)).assemble().push([(40,-40)]).circle(60).finalize().extrude(-77)