import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().segment((-51,-92),(-39,-74)).segment((-18,-93)).segment((-23,-100)).arc((3,11),(-51,-92)).assemble().reset().face(w0.sketch().segment((-12,86),(-4,30)).segment((27,34)).segment((21,90)).close().assemble()).finalize().extrude(-107).union(w0.sketch().segment((61,-21),(79,-21)).segment((79,9)).segment((61,9)).segment((61,-10)).segment((63,-10)).segment((63,-13)).segment((61,-13)).close().assemble().finalize().extrude(32)).union(w1.workplane(offset=77/2).moveTo(49,79).cylinder(77,21))