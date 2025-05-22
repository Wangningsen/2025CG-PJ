import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
w1=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().segment((48,-18),(61,-30)).segment((93,7)).segment((67,30)).segment((67,-18)).close().assemble().finalize().extrude(66).union(w1.sketch().segment((-100,-24),(-77,-24)).segment((-77,-56)).segment((-12,-56)).segment((-12,-93)).segment((82,-93)).segment((82,-57)).segment((53,-57)).segment((53,17)).segment((-1,17)).segment((-1,41)).segment((-24,41)).segment((-24,72)).segment((-77,72)).segment((-77,41)).segment((-100,41)).close().assemble().finalize().extrude(-9))