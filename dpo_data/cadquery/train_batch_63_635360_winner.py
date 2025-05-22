import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
w1=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().segment((-74,-82),(-11,-82)).segment((8,-100)).segment((74,-49)).segment((28,12)).segment((-2,-10)).arc((26,-67),(-23,-26)).segment((-37,-37)).segment((-23,-56)).segment((-74,-56)).segment((-74,-65)).segment((-66,-63)).segment((-66,-65)).segment((-74,-67)).close().assemble().finalize().extrude(-54).union(w1.sketch().segment((24,4),(100,4)).segment((100,31)).segment((50,31)).arc((36,46),(24,30)).close().assemble().finalize().extrude(65))