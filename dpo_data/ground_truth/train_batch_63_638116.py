import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
w1=cq.Workplane('XY',origin=(0,0,-68))
r=w0.sketch().segment((-26,69),(12,34)).segment((40,65)).segment((2,100)).close().assemble().finalize().extrude(29).union(w0.sketch().arc((-53,-46),(-19,-59),(-27,-95)).arc((38,-28),(-53,-46)).assemble().push([(-5,-51)]).circle(6,mode='s').finalize().extrude(51)).union(w1.workplane(offset=15/2).moveTo(-67.5,46.5).box(9,13,15))