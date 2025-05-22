import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().arc((-15,-33),(-12,-33),(-14,-35)).arc((49,-29),(13,23)).segment((13,19)).segment((-1,19)).arc((-20,-4),(-15,-33)).assemble().push([(-4,-13)]).circle(3,mode='s').finalize().extrude(-110).union(w0.workplane(offset=83/2).moveTo(-42.5,60.5).box(21,21,83)).union(w1.workplane(offset=80/2).moveTo(45.5,-19).box(9,104,80))