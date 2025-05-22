import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
w1=cq.Workplane('XY',origin=(0,0,-32))
r=w0.sketch().push([(40,-61)]).circle(32).push([(43,-30)]).circle(3,mode='s').finalize().extrude(54).union(w0.workplane(offset=57/2).moveTo(-57,50).cylinder(57,43)).union(w1.sketch().arc((-36,48),(-90,3),(-22,-20)).segment((23,-20)).segment((23,30)).segment((66,30)).segment((66,38)).segment((90,38)).segment((90,59)).segment((66,59)).segment((66,100)).segment((-8,100)).segment((-8,59)).segment((-32,59)).segment((-32,48)).close().assemble().finalize().extrude(-7))