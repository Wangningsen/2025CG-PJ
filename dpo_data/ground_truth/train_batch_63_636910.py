import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
r=w0.sketch().arc((-65,15),(-55,-74),(-51,16)).segment((-51,74)).segment((-65,74)).close().assemble().push([(-57,-28.5)]).rect(74,11,mode='s').reset().face(w0.sketch().segment((55,41),(88,-3)).segment((100,6)).segment((67,49)).close().assemble()).finalize().extrude(9)