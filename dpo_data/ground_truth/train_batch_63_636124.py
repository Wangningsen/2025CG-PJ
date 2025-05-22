import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
w1=cq.Workplane('XY',origin=(0,0,-85))
r=w0.sketch().push([(6,15)]).circle(22).reset().face(w0.sketch().arc((1,28),(3,2),(15,25)).arc((10,36),(1,28)).assemble(),mode='s').finalize().extrude(20).union(w1.sketch().push([(0,-18)]).rect(200,20).push([(39.5,-25.5)]).rect(5,3,mode='s').finalize().extrude(171))