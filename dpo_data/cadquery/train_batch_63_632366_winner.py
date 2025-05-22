import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,3))
w1=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.sketch().segment((-100,4),(-79,-29)).segment((-74,-26)).segment((-74,-31)).segment((24,-32)).segment((24,1)).segment((-4,11)).segment((28,44)).segment((9,73)).segment((-55,29)).segment((-74,37)).segment((-74,18)).close().assemble().finalize().extrude(-30).union(w0.sketch().segment((-71,-95),(41,-96)).segment((41,-90)).arc((85,-12),(9,-51)).segment((-71,-51)).close().assemble().finalize().extrude(12)).union(w1.workplane(offset=123/2).moveTo(0,-29).box(94,50,123))