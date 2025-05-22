import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().push([(8,34)]).circle(66).circle(25,mode='s').finalize().extrude(-78).union(w0.sketch().segment((-75,-100),(32,-100)).segment((32,-60)).segment((66,-60)).segment((66,74)).segment((32,74)).segment((32,79)).segment((-42,79)).segment((-42,74)).segment((-51,74)).segment((-51,4)).segment((-75,4)).close().assemble().finalize().extrude(-64)).union(w1.sketch().push([(8,34)]).circle(15).circle(5,mode='s').finalize().extrude(26))