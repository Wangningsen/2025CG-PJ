import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((-56,-30),(-20,-39),(15,-56)).arc((19,-58),(22,-61)).segment((56,-61)).segment((56,61)).segment((-56,61)).close().assemble().push([(42,-12)]).circle(10,mode='s').finalize().extrude(-200)