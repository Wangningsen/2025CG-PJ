import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
w1=cq.Workplane('YZ',origin=(49,0,0))
r=w0.sketch().segment((15,-48),(77,-48)).segment((77,78)).arc((96,89),(76,97)).segment((15,97)).close().assemble().push([(46,25)]).circle(3,mode='s').finalize().extrude(-112).union(w0.sketch().arc((19,43),(35,48),(24,35)).arc((85,83),(19,43)).assemble().finalize().extrude(59)).union(w1.workplane(offset=-146/2).moveTo(-57.5,38).box(85,102,146))