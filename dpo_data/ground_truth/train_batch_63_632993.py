import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=-89/2).moveTo(44,74).box(50,48,89).union(w0.sketch().arc((-53,20),(-22,51),(-51,83)).close().assemble().push([(9,16)]).circle(5).reset().face(w0.sketch().segment((10,15),(12,15)).segment((13,18)).segment((10,18)).close().assemble(),mode='s').finalize().extrude(-49)).union(w0.sketch().push([(-71,-69)]).circle(29).push([(3,9)]).circle(14).circle(4,mode='s').finalize().extrude(70)).union(w1.workplane(offset=75/2).moveTo(25,62).cylinder(75,38))