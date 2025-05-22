import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((43,80),(-73,-58),(88,21)).arc((86,64),(43,80)).assemble().push([(54,40)]).circle(23,mode='s').finalize().extrude(-200)