import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
w1=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().segment((-74,-82),(-11,-82)).segment((-11,-76)).segment((7,-100)).segment((74,-49)).segment((28,12)).segment((-2,-10)).arc((25,-68),(-23,-26)).segment((-39,-39)).segment((-26,-56)).segment((-74,-56)).close().assemble().push([(-70,-63)]).circle(4,mode='s').finalize().extrude(-53).union(w1.sketch().segment((24,4),(100,4)).segment((100,30)).segment((50,30)).arc((38,46),(26,30)).segment((24,30)).close().assemble().finalize().extrude(-65))