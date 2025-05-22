import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().segment((3,-75),(27,-75)).arc((51,-83),(77,-75)).segment((100,-75)).segment((100,-2)).segment((77,-2)).arc((51,6),(27,-2)).segment((3,-2)).close().assemble().push([(83,-66)]).circle(9,mode='s').finalize().extrude(-98).union(w0.workplane(offset=99/2).moveTo(-93,68.5).box(14,29,99))