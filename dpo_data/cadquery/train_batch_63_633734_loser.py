import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().push([(41,26)]).circle(31).circle(24,mode='s').finalize().extrude(-91).union(w0.sketch().segment((-72,31),(-25,-78)).segment((59,-42)).segment((52,-26)).segment((62,-26)).segment((55,78)).segment((22,76)).segment((24,40)).segment((15,69)).close().assemble().finalize().extrude(109))