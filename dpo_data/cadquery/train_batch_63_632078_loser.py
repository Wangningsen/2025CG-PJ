import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-37))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().arc((-50,30),(-53,-5),(-20,10)).segment((42,10)).segment((42,100)).segment((-50,100)).close().assemble().push([(-38,15)]).circle(14,mode='s').finalize().extrude(-30).union(w0.sketch().segment((1,-100),(35,-100)).segment((35,-91)).arc((61,-49),(35,-7)).segment((35,2)).segment((1,2)).segment((1,-7)).arc((-24,-49),(1,-91)).close().assemble().push([(19,-49)]).circle(16,mode='s').finalize().extrude(9)).union(w1.workplane(offset=3/2).moveTo(-11.5,19.5).box(83,97,3))