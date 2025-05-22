import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
r=w0.sketch().arc((-32,1),(-72,-89),(7,-30)).arc((66,86),(-32,1)).assemble().push([(20,-75)]).circle(3).finalize().extrude(63)