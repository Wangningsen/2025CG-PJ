import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.workplane(offset=-161/2).moveTo(18,0).cylinder(161,82).union(w0.sketch().segment((-25,-54),(-25,-39)).segment((59,-39)).arc((74,-6),(66,29)).arc((55,38),(46,49)).arc((30,55),(13,57)).arc((-97,32),(-25,-54)).assemble().push([(-34,11)]).circle(19,mode='s').finalize().extrude(-141))