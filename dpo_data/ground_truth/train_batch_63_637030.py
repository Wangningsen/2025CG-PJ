import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
r=w0.sketch().arc((-22,-32),(5,-100),(27,-30)).arc((-3,100),(-22,-32)).assemble().push([(1,-81)]).circle(14,mode='s').finalize().extrude(-17)