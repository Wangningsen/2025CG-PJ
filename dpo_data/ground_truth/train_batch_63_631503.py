import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().segment((-100,-60),(9,-60)).segment((9,-55)).arc((84,-55),(85,20)).segment((79,70)).segment((1,61)).segment((3,44)).segment((-100,44)).close().assemble().reset().face(w0.sketch().arc((38,-27),(49,-30),(58,-25)).close().assemble(),mode='s').finalize().extrude(-34)