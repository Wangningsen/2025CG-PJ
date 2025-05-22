import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
r=w0.sketch().segment((-99,-9),(-81,16)).segment((-7,-17)).segment((-52,-79)).segment((-52,-81)).arc((84,-50),(65,80)).arc((10,14),(-40,96)).arc((-88,52),(-99,-9)).assemble().finalize().extrude(-68)