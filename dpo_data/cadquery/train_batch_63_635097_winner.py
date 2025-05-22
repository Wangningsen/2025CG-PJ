import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().arc((-35,41),(-86,-62),(26,-36)).arc((55,-27),(76,-5)).arc((100,10),(83,28)).arc((28,84),(-35,41)).assemble().push([(81,13)]).circle(7,mode='s').finalize().extrude(-90)